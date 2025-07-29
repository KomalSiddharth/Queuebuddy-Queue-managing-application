/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}"
  ],
  theme: {
    extend: {
      fontFamily: {
      pacifico: ['Pacifico', 'cursive'],
      rubik: ['Rubik', 'sans-serif']
    },
  },
  plugins: [],
}
}
