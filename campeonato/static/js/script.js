
import { createClient } from '@supabase/supabase-js'
const supabaseUrl = 'https://ylviircdnwgxuczbczlq.supabase.co'
const supabaseKey = process.env.SUPABASE_KEY
const supabase = createClient(supabaseUrl, supabaseKey)

document.addEventListener("DOMContentLoaded", function() {
        

    const loginButton = document.getElementById("submitLogin");
    const loginForm = document.getElementById("loginForm");
    const loginError = document.getElementById("loginError");

    // Evento para manejar el botón "Ingresar"
    loginButton.addEventListener("click", async function(event) {
        event.preventDefault();  // Evita el envío directo del formulario

        // Obtener datos del formulario
        const email = loginForm.email.value;
        const password = loginForm.password.value;

        // Llamar a Supabase para autenticación
        const { data, error } = await supabase.auth.signInWithPassword({
            email: email,
            password: password
        });

        // Manejo de resultado
        if (error) {
            loginError.textContent = "Error: " + error.message;
        } else {
            loginError.textContent = "";
            window.location.href = "{% url 'sesioniniciada' %}";
        }
    });
});