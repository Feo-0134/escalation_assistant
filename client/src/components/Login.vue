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
        <v-col cols="12" sm="8" md="10">
          <v-text-field
            placeholder="username"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="8" md="10">
          <v-text-field
            v-model="password"
            :append-icon="showPasswd ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="showPasswd ? 'text' : 'password'"
            name="input-10-1"
            label="Password"
            counter
            @click:append="showPasswd = !showPasswd"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="10" md="12">
            <v-btn large color="primary" @click="login2Dsh()">Login</v-btn>
        </v-col>
      </v-col>
     </v-card-text>
    </v-card>

    </v-row>
  </v-container>  
</template>
<script>
export default {
    data:()=>({
        showPasswd: false,
        password: null,
        rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 8 || 'Min 8 characters',   
        },
    }),
    methods: {
      login2Dsh() {
        this.$router.push(`/dsh`)
      },
    }
}
</script>