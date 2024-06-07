import { createRouter, createWebHistory } from 'vue-router'
import Home from "@/components/Home.vue";
import Tours from "@/components/Tours.vue";
import Contact from "@/components/Contact.vue";
import Services from "@/components/Services.vue";
import AboutUs from "@/components/AboutUs.vue";
import Excursions from "@/components/Excursions.vue";
import Login from "@/components/admin/Login.vue";
import AdminPage from "@/components/admin/AdminPage.vue";

const routes = [
    { path: '/', component: Home },
    { path: '/tours', component: Tours },
    { path: '/contact', component: Contact },
    { path: '/services', component: Services },
    { path: '/about-us', component: AboutUs },
    { path: '/excursions', component: Excursions },
    { path: '/login', component: Login},
    { path: '/admin', component: AdminPage}
];

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
