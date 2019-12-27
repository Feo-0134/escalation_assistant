<template>
    <v-container
      class="fill-height"
      fluid
    >
      <v-row class="d-flex flex-column"
      >
      <Comment4Edit v-for="p in cmt_list" class="pa-2" :key="p._id"
      :pindex="index" :comment_pk="p.id"></Comment4Edit>
      </v-row>
      </v-container>
</template>
<script>
import Comment4Edit from '@/components/Comment4Edit'
export default {
    components: { Comment4Edit },
    asyncComputed: {
      cmt_list: {
        async get() {
          try {
            const res = await this.$http.get(
              'http://localhost:8000/assistant/comment/',{
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
}
</script>