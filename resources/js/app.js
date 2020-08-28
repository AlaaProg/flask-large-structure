import Vue from "vue";


Vue.component("v-hello", ()=> import("@components/HelloWorld.vue"));

new Vue({
	el:'#app',
})