const navToggle = document.querySelector('#navbar-toggle')
const navbarItems = document.querySelector('#navbar-items')
const themeToggle = document.querySelector('#theme-toggle')

navToggle.addEventListener('click', () => {
    navbarItems.classList.toggle('hidden')
})

themeToggle.addEventListener('click', () => {
    document.documentElement.classList.toggle('dark')

    if (document.documentElement.classList.contains('dark')) {
        themeIcon.classList.replace('fa-moon', 'fa-sun')
        localStorage.theme = 'dark'
    } else {
        themeIcon.classList.replace('fa-sun', 'fa-moon')
        localStorage.theme = 'light'
    }

    // Whenever the user explicitly chooses to respect the OS preference
    // localStorage.removeItem('theme')
})
