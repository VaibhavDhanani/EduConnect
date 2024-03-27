// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-app.js";
import {
	getAuth,
	createUserWithEmailAndPassword,
	signInWithEmailAndPassword,
} from "https://www.gstatic.com/firebasejs/10.7.2/firebase-auth.js";
import { getDatabase , ref, set } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-database.js";
import  {getFirestore, collection, getDoc ,doc , setDoc } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-firestore.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
	apiKey: "AIzaSyDoKKxEn-IChCtdV8BuoohMf7TMZyZXZxk",
	authDomain: "educonnect-6789e.firebaseapp.com",
	databaseURL: "https://educonnect-6789e-default-rtdb.firebaseio.com",
	projectId: "educonnect-6789e",
	storageBucket: "educonnect-6789e.appspot.com",
	messagingSenderId: "422805237793",
	appId: "1:422805237793:web:7fcf5afa6d241f935b3360",
	measurementId: "G-XHXM785F62"
};
// Initialize Firebase
const login = {
	getAuth,
	createUserWithEmailAndPassword,
	signInWithEmailAndPassword,
};
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);
document.addEventListener("DOMContentLoaded", function () {
	const container = document.getElementById('container');
	const registerBtn = document.getElementById('register');
	const loginBtn = document.getElementById('login');

	registerBtn.addEventListener('click', () => {
		container.classList.add("active");
	});

	loginBtn.addEventListener('click', () => {
		container.classList.remove("active");
	});

	let info_update = (name, email, role, uid) => {

		const docref = doc(db, "User", uid);
		setDoc(docref, {
			name: name,
			email: email,
			role: role,
		})

	}


	//! sign up code using firebase email/password method
	const signup = document.getElementById("formSignup");
	signup.addEventListener("submit", function (event) {
		event.preventDefault();
		const name = signup["name"].value;
		const email = signup["email"].value;
		const password = signup["password"].value;
		const role = document.getElementById("role").value

		createUserWithEmailAndPassword(auth, email, password)
			.then(async (userCredential) => {

				await info_update(name , email, role, userCredential.user.uid)
				let uid = userCredential.user.uid;
				document.cookie = `uid=${uid}`
				document.cookie = `name=${name}`
				document.cookie = `role=${role}`
				window.location.href = "home/";
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

		const email = signin["email"].value;
		const password = signin["password"].value;

		signInWithEmailAndPassword(auth, email, password)
			.then(async (userCredential) => {
				let uid = userCredential.user.uid;
				const docref = doc(db, "User", uid);
				await getDoc(docref).then((doc) => {
					if (doc.exists()) {
						console.log("Document data:", doc.data());
						document.cookie = `name=${doc.data().name}`
						document.cookie = `role=${doc.data().role}`

					} else {
						// doc.data() will be undefined in this case
						console.log("No such document!");
					}
				});
				document.cookie = `uid=${uid}`
				window.location.href = "home/";
			})
			.catch((error) => {
				const errorCode = error.code;
				const errorMessage = error.message;
			});
	});
});
