Vue.use(VeeValidate);
Vue.component('modal', {
  template: '#modal-template'
});

// start app
new Vue({
  delimiters: ['[[', ']]'],
  el: '#objective',
  data: {
    showModal: false,
    showDeleteModal: false,
    objectives: [],
    programs_list: [],
    name: '',
    description: '',
    parent_id: '',
    program_id: '',
    parent_obj_list: [],
    isEdit: false,
    currentObjective: null,
    itemToDelete: null,
    modalHeader: 'Add objective'
  },
  beforeMount: function() {
    this.makeRequest('GET', '/indicators/objective/')
      .then(response => {
        if (response.data) {
          console.log('response', response);
          this.objectives = response.data
            .slice()
            .sort((a, b) => b.id - a.id)
            .map(el => {
              el['program_id'] = el['program'];
              el['parent_id'] = el['parent'];
              delete el['program'];
              delete el['parent'];
              return el;
            });
          // this.parent_obj_list = response.data
          //   .sort((a, b) => b.id - a.id)
          // .map(el => {
          //   el['program_id'] = el['program'];
          //   el['parent_id'] = el['parent'];
          //   delete el['program'];
          //   delete el['parent'];
          //   return el;
          // });
          this.parent_obj_list = this.objectives;
          console.log('objectives list', this.objectives);
          console.log('parent list', this.parent_obj_list);
          $(document).ready(() => {
            $('#objectivesTable').DataTable({
              pageLength: 10,
              lengthMenu: [10, 20, 30, 40]
            });
          });
        }
      })
      .catch(e => {
        toastr.error('There was a problem loading data from the database');
        this.objectives = [];
      });

    this.makeRequest('GET', '/workflow/level1_program/')
      .then(response => {
        if (response.data) {
          console.log('wfl1 response', response.data);
          this.programs_list = response.data.map(el => {
            el['program_id'] = el['id'];
            delete el['id'];
            return el;
          });
          this.programs_list = response.data;
        }
        console.log('program list', this.programs_list);
      })
      .catch(e => {
        toastr.error('There was a problem loading data from the database');
      });
  },
  methods: {
    /**
     * open or close the objective form modal
     * @param { object } item - objective item
     */
    toggleModal: function(item = null) {
      this.showModal = !this.showModal;
      if (item) {
        this.isEdit = true;
        this.modalHeader = `Edit ${item.name}`;
        this.currentObjective = item;
        this.name = item.name;
        this.description = item.description;
        this.program_id = item.program_id;
        this.parent_id = item.parent_id;
        this.parent_obj_list = this.objectives.filter(el => el.id !== item.id);
        console.log('current obj', this.currentObjective);
      } else {
        this.isEdit = false;
        this.name = '';
        this.description = '';
        this.program_id = '';
        this.parent_id = '';
        this.modalHeader = 'Add objective';
        this.parent_obj_list = this.objectives;
      }
    },

    /**
     * open or close the objective delete modal
     * @param { object } data - objective item
     */
    toggleDeleteModal: function(data) {
      this.showDeleteModal = !this.showDeleteModal;
      if (data) {
        this.modalHeader = 'Confirm delete';
        this.itemToDelete = data;
      } else {
        this.modalHeader = 'Add objective';
      }
    },

    /**
     * Format date
     * @param {string} date - date to be formatted
     */
    formatDate: function(date) {
      return moment(date, 'YYYY-MM-DDThh:mm:ssZ').format('YYYY-MM-DD');
    },

    /**
     * process form data
     * @param { boolean } saveNew - true to keep the modal open for additional posts
     */
    processForm: function(saveNew = false) {
      this.$validator.validateAll().then(result => {
        if (result) {
          if (this.currentObjective && this.currentObjective.id) {
            this.updateObjective();
          } else {
            if (saveNew) {
              this.postData(saveNew);
            } else {
              this.postData();
            }
          }
        }
      });
    },

    /**
     * Create new objective
     * @param { boolean } saveNew - true if a user wants to make multiple posts
     */
    async postData(saveNew) {
      try {
        const response = await this.makeRequest(
          'POST',
          `/indicators/objective/`,
          {
            name: this.name,
            description: this.description,
            parent: this.parent_id,
            program: this.program_id
          }
        );
        if (response) {
          toastr.success('Objective is saved');
          response.data['program_id'] = response.data['program'];
          response.data['parent_id'] = response.data['parent'];
          delete response.data['program'];
          delete response.data['parent'];
          this.objectives.unshift(response.data);
          if (!saveNew) {
            this.toggleModal();
          }
          // resetting the form
          this.name = '';
          this.description = '';
          this.program_id = '';
          this.parent_id = '';
          this.$validator.reset();
        }
      } catch (error) {
        toastr.error('There was a problem saving');
      }
    },

    /**
     * Edit objective item
     */
    async updateObjective() {
      try {
        const response = await this.makeRequest(
          'PATCH',
          `/indicators/objective/${this.currentObjective.id}`,
          {
            name: this.name,
            description: this.description,
            parent: this.parent_id,
            program: this.program_id
          }
        );
        if (response) {
          console.log('update response', response.data);
          toastr.success('Objective is updated');
          response.data['program_id'] = response.data['program'];
          response.data['parent_id'] = response.data['parent'];
          delete response.data['program'];
          delete response.data['parent'];
          const newObjectives = this.objectives.filter(item => {
            return item.id != this.currentObjective.id;
          });
          this.objectives = newObjectives;
          this.objectives.unshift(response.data);
          console.log('update objective', this.objectives);
          console.log('edited objective', response.data);
          this.isEdit = false;
          this.name = '';
          this.description = '';
          this.program_id = '';
          this.parent_id = '';
          this.currentObjective = null;
          this.modalHeader = 'Add Objective';
          this.toggleModal();
        }
      } catch (e) {
        toastr.error('There was a problem updating this');
      }
    },

    /**
     * Delete objective
     * @param { number } id - id of the objective to be deleted
     */
    async deleteObjective(id) {
      try {
        const response = await this.makeRequest(
          'DELETE',
          `/indicators/objective/${id}`
        );
        if (response.status === 204) {
          toastr.success('Objective is deleted');
          this.objectives = this.objectives.filter(item => +item.id !== +id);
          this.showDeleteModal = !this.showDeleteModal;
          this.modalHeader = 'Add Objective';
        } else {
          toastr.error('There was a problem deleting this');
        }
      } catch (error) {
        toastr.error('There was a server error');
      }
    },

    /**
     * make requests for CRUD operations using axios
     * @param { string } method - request method
     * @param { string } url  - request url
     * @param { string } data - request payload
     * @return { Promise } - axios response Promise
     */
    makeRequest(method, url, data = null) {
      axios.defaults.xsrfHeaderName = 'X-CSRFToken';
      axios.defaults.xsrfCookieName = 'csrftoken';
      return axios({ method, url, data });
    }
  },

  computed: {
    /**
     * Check if objective form is valid
     */
    isFormValid() {
      return this.name;
    }
  }
});
