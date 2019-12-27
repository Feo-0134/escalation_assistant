<template>
    <v-container
        id="input-usage"
        fluid
    >
        <v-row>
        <v-card
            class="mt-12 mx-auto"
            color="rgb(48, 48, 48)"
            cols="12" sm="8" md="6"
            
        >
        <v-card-text>
        <v-col cols="12">
            <v-toolbar>
                <v-toolbar-title>
                </v-toolbar-title>
                <v-toolbar-items

                >
                <v-text-field
                    v-model="processKind"
                    disabled
                >{{ processKind }}</v-text-field>
                <v-menu offset-y>
                <template v-slot:activator="{ on }">
                    <v-btn
                    class="grey darken-2 ml-3"
                    dark
                    v-on="on"
                    >
                    <v-icon >mdi-chevron-down</v-icon>
                    </v-btn>
                </template>
                <v-list>
                    <v-list-item
                    v-for="(item, index) in items"
                    :key="index"
                    @click="processKind=item.title"
                    >
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                    </v-list-item>
                </v-list>
                </v-menu>
                </v-toolbar-items>
            </v-toolbar>
            <v-col cols="12" sm="10" md="12">
                <v-btn  class="mx-4" large color="primary" @click="initNewProcess()">Apply</v-btn>
            </v-col>
        </v-col>
        </v-card-text>
        </v-card>

        </v-row>
    </v-container>  
</template>
<script>
export default {
    data: () => ({
      processKind: '',
      items: [
        { title: 'SE --> SEE' },
        { title: 'SEE --> EE' },
        { title: 'Other' },
      ],
    }),
    computed:{
        processtitle() {
            return this.processKind==='SE --> SEE' ? 'E0' : 'E1'
        }
    },
    methods: {
      async initNewProcess() {
        try {
          // let that = this
          const res = await this.$http.post(
            'http://localhost:8000/assistant/process/',
              {
                title: this.processtitle,
                engineer: 1,
                status: "S1",
                owner: 2
              },
              {
                auth: {
                  username:"test_su0",
                  password:"!QA2ws3ed"
                }
              }
          );
          location.reload();
          return res.data
        }catch(e) {
          window.console.log(e);
        }
      }
    }
}
</script>