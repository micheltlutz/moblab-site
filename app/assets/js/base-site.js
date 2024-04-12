document.addEventListener('DOMContentLoaded', (event) => {
    const bodyElement = document.body;
    const darkModeIcon = document.getElementById('dark-mode-icon');
    const lightModeIcon = document.getElementById('light-mode-icon');

    // Inicializa o tema escuro por padrão
    bodyElement.classList.remove('light-mode');

    darkModeIcon.addEventListener('click', () => {
        bodyElement.classList.remove('light-mode');
    });

    lightModeIcon.addEventListener('click', () => {
        bodyElement.classList.add('light-mode');
    });
});