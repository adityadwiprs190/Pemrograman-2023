const validEmail = 'ahmad2017' ;
const validPassword = 'integrity' ;

function validatelogin() {
    const enteredEmail = document.getElementById('staticemail').value ;
    const enteredPassword = document.getElementById('inputPassword').value ;

 if (enteredEmail === validEmail && enteredPassword === validPassword) {
     window.location.href= 'Project Toko busana/tokobusana.html' ;
     alert('Login Sukses');
} else {
     alert('Login Gagal');
}

}

   