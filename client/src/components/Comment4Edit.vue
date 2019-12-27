<template>
  <v-container>
    <!-- {{comment}} -->
  <v-card
    class="mx-auto"
    max-width="344"
    outlined
  >
    <v-list-item three-line>
      <v-list-item-content>
        <div class="overline mb-4">{{comment.result}}</div>
        <v-list-item-title class="headline mb-1">{{comment.id}}-{{comment.engineer}}-{{comment.stageTitle}}</v-list-item-title>
        <v-list-item-subtitle class="mt-6">
        <v-textarea
          class="mt-4"
          outlined
          name="input-7-4"
          label="Outlined textarea"
          v-model="comment.comment_text"
        ></v-textarea>
        </v-list-item-subtitle>
      </v-list-item-content>

      <v-list-item-avatar
        tile
        size="80"
        color="grey"
      ></v-list-item-avatar>
    </v-list-item>

    <v-card-actions>
      <v-btn text>Save</v-btn>
    </v-card-actions>
  </v-card>
  </v-container>
</template>

<script>
export default {
    props: {
        comment_pk: Number,
    },
    data: ()=> ({
    }),
    computed: {
      cmt_pk() {
        if(this.comment_pk)
          return this.comment_pk
        else
          return this.$route.path.split('/')[1]
      }
    },
    asyncComputed: {
      comment: {
        async get() {
          try {
            const res = await this.$http.get(`http://localhost:8000/assistant/comment/${this.cmt_pk}`);
            return res.data
          }catch(e) {
            // console.log(e);
          }
        },
        default () {
            return {} // for typeError: no default value
        }
      }
    },

}
</script>
