// tech-prep-hub/static/js/main.js

document.addEventListener('DOMContentLoaded', () => {
    console.log('main.js loaded!');

    // Accordion functionality for Previous Papers and Interview Questions
    const accordionHeaders = document.querySelectorAll('.accordion-header');

    accordionHeaders.forEach(header => {
        header.addEventListener('click', () => {
            const content = header.nextElementSibling; // This is the accordion-content div
            const icon = header.querySelector('.accordion-icon');

            // Toggle the current accordion
            content.classList.toggle('hidden');
            icon.classList.toggle('rotate-180'); // Rotate arrow icon
        });
    });

    // Nested accordion functionality for Interview Questions (Q&A inside categories)
    const questionToggles = document.querySelectorAll('.question-toggle');

    questionToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const answerContent = toggle.nextElementSibling; // This is the answer-content div
            const arrowIcon = toggle.querySelector('.arrow-icon');

            answerContent.classList.toggle('hidden');
            arrowIcon.classList.toggle('rotate-180');
        });
    });

    // Solution Toggle functionality for Problems page
    const solutionToggles = document.querySelectorAll('.solution-toggle');

    solutionToggles.forEach(button => {
        button.addEventListener('click', () => {
            const solutionContent = button.nextElementSibling; // This is the solution-content div
            const icon = button.querySelector('.solution-icon');

            solutionContent.classList.toggle('hidden');
            icon.classList.toggle('rotate-180');

            // Change button text and color based on state
            if (solutionContent.classList.contains('hidden')) {
                button.innerHTML = 'Show Solution <svg class="w-5 h-5 ml-2 transform transition-transform duration-300 solution-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>';
                button.classList.remove('bg-red-600', 'hover:bg-red-700'); // Remove red color
                button.classList.add('btn-primary'); // Apply primary button style
            } else {
                button.innerHTML = 'Hide Solution <svg class="w-5 h-5 ml-2 transform rotate-180 transition-transform duration-300 solution-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>';
                button.classList.remove('btn-primary'); // Remove primary button style
                button.classList.add('bg-red-600', 'hover:bg-red-700'); // Apply red color
            }
        });
    });
});