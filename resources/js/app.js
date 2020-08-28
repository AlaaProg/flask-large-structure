import Vue from "vue";



Vue.component("v-hello", ()=> import("@components/HelloWorld.vue"));
Vue.component("v-test", ()=> import("@components/Test.vue"));


new Vue({
	el:'#app',
})