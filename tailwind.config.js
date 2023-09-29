/** @type {import('tailwindcss').Config} */

const path = require('path')

const projectPaths = ['./templates/**/*.html']
let sitePackagesPath = 'venv/lib/python3.11/site-packages/'

pyPackagePaths = [
    path.join(sitePackagesPath, 'crispy_tailwind/**/*.html'),
    path.join(sitePackagesPath, 'crispy_tailwind/**/*.py'),
    path.join(sitePackagesPath, 'crispy_tailwind/**/*.js'),
]

module.exports = {
    content: [...projectPaths, ...pyPackagePaths],
    darkMode: 'class',
    theme: {
        extend: {},
    },
    plugins: [require('@tailwindcss/forms')],
}
