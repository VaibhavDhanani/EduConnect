
    // Import the functions you need from the SDKs you need
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-app.js";
    import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-analytics.js";
    // TODO: Add SDKs for Firebase products that you want to use
    // https://firebase.google.com/docs/web/setup#available-libraries

    // Your web app's Firebase configuration
    // For Firebase JS SDK v7.20.0 and later, measurementId is optional
    const firebaseConfig = {
    apiKey: "AIzaSyDoKKxEn-IChCtdV8BuoohMf7TMZyZXZxk",
    authDomain: "educonnect-6789e.firebaseapp.com",
    projectId: "educonnect-6789e",
    storageBucket: "educonnect-6789e.appspot.com",
    messagingSenderId: "422805237793",
    appId: "1:422805237793:web:7fcf5afa6d241f935b3360",
    measurementId: "G-XHXM785F62"
};

    // Initialize Firebase
    const app = initializeApp(firebaseConfig);
    export {app}
