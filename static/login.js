// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-app.js";
import {
	getAuth,
	createUserWithEmailAndPassword,
	signInWithEmailAndPassword,
} from "https://www.gstatic.com/firebasejs/10.7.2/firebase-auth.js";
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
	measurementId: "G-XHXM785F62",
};

// Initialize Firebase
const login = {
	getAuth,
	createUserWithEmailAndPassword,
	signInWithEmailAndPassword,
};
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
document.addEventListener("DOMContentLoaded", function () {
	const container = document.getElementById("container");
	const signIn = document.getElementById("signIn-updated");
	const signUp = document.getElementById("signup-updated");

	signUp.addEventListener("click", function () {
		container.classList.add("right-active");
		// console.log("added");
	});

	signIn.addEventListener("click", function () {
		container.classList.remove("right-active");
		// console.log("removed");
	});

	//! sign up code using firebase email/password method
	const signup = document.getElementById("formSignup");
	signup.addEventListener("submit", function (event) {
		event.preventDefault();
		const name = signup["name"].value;
		const email = signup["email"].value;
		const password = signup["password"].value;
		console.log(name, email, password);

		createUserWithEmailAndPassword(auth, email, password)
			.then((userCredential) => {
				window.location.href = "index.html";
			})
			.catch((error) => {
				const errorCode = error.code;
				const errorMessage = error.message;
			});
	});

	//! sign in code using firebase email/password method
	const signin = document.getElementById("formSignin");

	signin.addEventListener("submit", function (event) {
		event.preventDefault();

		const email = signin["Email"].value;
		const password = signin["Password"].value;

		signInWithEmailAndPassword(auth, email, password)
			.then((userCredential) => {
				window.location.href = "index.html";
			})
			.catch((error) => {
				const errorCode = error.code;
				const errorMessage = error.message;
			});
	});
});
