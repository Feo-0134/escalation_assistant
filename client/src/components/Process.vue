<template>
    <div>
        <!-- <p>{{comment_list}}</p>  -->
        <v-toolbar>
            <template v-if="$vuetify.breakpoint.smAndUp">
                <v-avatar color="indigo" size="36" class="mx-auto">
                    <span class="white--text">{{shortName}}</span>
                </v-avatar>
            </template>
            <v-toolbar-title 
            >
                <p class="mx-5 mt-4">
                    {{p_title}} - {{engineer.name}} - {{process.status}}
                </p>
            </v-toolbar-title>

            <v-spacer></v-spacer>

            <v-toolbar-items>
                <v-btn class="mx-8" v-if="assigned" icon @click="showMore()"> 
                    <v-icon >mdi-chevron-down</v-icon>
                    More 
                </v-btn>
                <v-btn class="mx-12" v-if="!assigned" icon @click="addReviewer()" >
                    <v-icon class="mx-2">mdi-account-multiple-plus-outline</v-icon>
                    Add Reviewer
                </v-btn>
            </v-toolbar-items>
        </v-toolbar>
        <v-stepper v-model="stage">
            <v-stepper-header>
                <v-stepper-step :complete="stage > 1" step="1">Submit Request</v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step :complete="stage > 2" step="2">Review Checklist</v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step :complete="stage > 3" step="3">Prepare Materials</v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step  step="4">Review Meeting</v-stepper-step>
            
            
            </v-stepper-header>

            <v-stepper-items v-show="detailShow == true">
                <v-stepper-content step="1">
                    <v-card
                    class="mb-12"
                    color="grey lighten-1"
                    height="200px"
                    >
                    <Comment
                       v-for="(p, index) in comment_list.related_comment" :key="p._id"
                        :pindex="index"
                        :comment_pk="p"
                    > </Comment>
                       <!-- {{comment_list}}-->
                    </v-card>

                    <v-btn color="primary"
                    @click="stage = 2"
                    >
                    Continue
                    </v-btn>

                    <v-btn text @click="showDetailComment()">Edit Process</v-btn>
                </v-stepper-content>

                <v-stepper-content step="2">
                    <v-card
                    class="mb-12"
                    color="grey lighten-1"
                    height="200px"
                    >
                    <Comment
                       v-for="(p, index) in comment_list.related_comment" :key="p._id"
                        :pindex="index"
                        :comment_pk="p"
                    > </Comment>
                       <!-- {{comment_list}}-->
                    </v-card>

                    <v-btn
                    color="primary"
                    @click="stage = 3"
                    >
                    Continue
                    </v-btn>

                    <v-btn text @click="showDetailComment()">Edit Process</v-btn>
                </v-stepper-content>

                <v-stepper-content step="3">
                    <v-card
                    class="mb-12"
                    color="grey lighten-1"
                    height="200px"
                    >
                    <Comment
                       v-for="(p, index) in comment_list.related_comment" :key="p._id"
                        :pindex="index"
                        :comment_pk="p"
                    > </Comment>
                       <!-- {{comment_list}}-->
                    </v-card>

                    <v-btn
                    color="primary"
                    @click="stage = 4"
                    >
                    Continue
                    </v-btn>

                    <v-btn text @click="showDetailComment()">Edit Process</v-btn>
                </v-stepper-content>
                
                <v-stepper-content step="4">
                    <v-card
                    class="mb-12"
                    color="grey lighten-1"
                    height="200px"
                    >
                    <Comment
                       v-for="(p, index) in comment_list.related_comment" :key="p._id"
                        :pindex="index"
                        :comment_pk="p"
                    > </Comment>
                       <!-- {{comment_list}}-->
                    </v-card>

                    <v-btn
                    color="primary"
                    @click="stage = 1"
                    >
                    Continue
                    </v-btn>

                    <v-btn text @click="showDetailComment()">Edit Process</v-btn>
                </v-stepper-content>
            </v-stepper-items>
        </v-stepper>
    </div>
</template>

<script>
    import Comment from '@/components/Comment'
    export default {
        props: {
            process: Object,
        },
        components: { Comment },
        data: () => ({
            stage: 1,
            assigned: true,
            detailShow: false,
            stage_id: null,
            shortName: 'loading ...'
        }),
        asyncComputed: {
            engineer: {
                async get() {
                    try {
                        const res = await this.$http.get(`http://127.0.0.1:8000/assistant/engineer/${this.process.engineer}`);
                        // console.log(res)
                        var nameArr = res.data.name.split(' ')
                        this.shortName = nameArr[0][0] + nameArr[nameArr.length - 1][0]
                        this.stage = parseInt(this.process.status.split('S')[1])
                        return res.data
                    }catch(e) {
                        // console.log(e);
                    }
                }   
            },
            comment_list: {
                async get() {
                try {
                    const res = await this.$http.get(`http://localhost:8000/assistant/stage/${this.process.stage[this.stage-1]}`);
                    return res.data
                }catch(e) {
                    // console.log(e);
                }
                },
                default () {
                    return [{fields:{title: 'undefined'}}] // for typeError: no default value
                }
            }
        },
        computed: {
            p_title() {
                if (this.process.title === 'E0')
                    return 'SEE Review Process'
                else if (this.process.title === 'E1')
                    return 'EE Review Process'
                return 'UnKnown'
            }
        },
        methods: {
            showMore() {
                // this.stage_id = (this.stage_list[this.stage - 1]).pk
                this.detailShow = !this.detailShow
            },
            showDetailComment() {
                this.$router.push(`/${this.process.stage[this.stage-1]}/cmt`) 
            }
        }
    }
</script>