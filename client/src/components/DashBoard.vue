<template>
    <v-container
      class="fill-height"
      fluid
    >
      <v-row
        justify="center"
      >
      <!-- {{process_list}} -->
      <Process v-for="(p, index) in process_list" :key="p._id"
      :pindex="index" :process="p"
      style="width: 85%"
      >
      </Process>
      </v-row>
        <v-card-text style="right:5px; bottom: 5px; position: absolute">
          <v-btn
            absolute
            dark
            fab
            top
            right
            color="pink"
            @click="initNewProcess()"
          >
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </v-card-text>
    </v-container>    
</template>

<script>
  import Process from '@/components/Process'
  export default {
    components: {Process},
    data: () => ({
      drawer: null,
      e1: 1,
      detailShow: false,
      user: 2
    }),
    asyncComputed: {
      process_list: {
        async get() {
          try {
            const res = await this.$http.get(
              'http://localhost:8000/assistant/process/',{
              auth: {
                username:"test_su0",
                password:"!QA2ws3ed"
              }}
            );
            return res.data.results
          }catch(e) {
            // console.log(e);
          }
        }
      }
    },
    created () {
      this.$vuetify.theme.dark = true
    },
    methods: {
      route(path) {
        if (path == 'apply') {
          this.$router.push(`/apply`)
        }
      },
      async initNewProcess() {
        try {
          // let that = this
          const res = await this.$http.post(
            'http://localhost:8000/assistant/process/',
              {
                title: "E0",
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
          // const res0 = await this.$http.post(
          //   'http://localhost:8000/assistant/stage/',
          //     {
          //       title: "E0",
          //       engineer: 1,
          //       status: "S1",
          //       owner: 2
          //     },
          //     {
          //       auth: {
          //         username:"test_su0",
          //         password:"!QA2ws3ed"
          //       }
          //     }
          // );
          // window.console.log(res0.data)
          location.reload();
          return res.data
        }catch(e) {
          window.console.log(e);
        }
      }
    }
  }
</script>