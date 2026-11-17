const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");

menuToggle.addEventListener("click", function () {
    navLinks.classList.toggle("active");

    const isOpen = navLinks.classList.contains("active");

    menuToggle.setAttribute("aria-expanded", isOpen);

    if (isOpen) {
        menuToggle.innerHTML = `
            <svg viewBox="0 0 24 24" aria-hidden="true">
                <path d="M6 6l12 12M18 6L6 18"></path>
            </svg>
        `;
    } else {
        menuToggle.innerHTML = `
            <svg viewBox="0 0 24 24" aria-hidden="true">
                <path d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
        `;
    }
});


const navItems = document.querySelectorAll(".nav-links a");

navItems.forEach(function (link) {
    link.addEventListener("click", function () {
        navLinks.classList.remove("active");

        menuToggle.setAttribute("aria-expanded", "false");

        menuToggle.innerHTML = `
            <svg viewBox="0 0 24 24" aria-hidden="true">
                <path d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
        `;
    });
});

/* =========================================================
   NAVBAR SECTION-BASED THEME
========================================================= */

const navbar = document.querySelector(".navbar");

const sections = document.querySelectorAll(
    "#home, #about, #skills, #experience, #projects, #contact"
);

const darkSections = ["about", "experience", "contact"];

const observerOptions = {
    root: null,
    rootMargin: "-20% 0px -60% 0px",
    threshold: 0
};

const sectionObserver = new IntersectionObserver(
    function (entries) {

        entries.forEach(function (entry) {

            if (entry.isIntersecting) {

                const sectionId = entry.target.id;

                if (darkSections.includes(sectionId)) {

                    navbar.classList.add("dark-theme");
                    navbar.classList.remove("light-theme");

                } else {

                    navbar.classList.add("light-theme");
                    navbar.classList.remove("dark-theme");

                }

            }

        });

    },
    observerOptions
);

sections.forEach(function (section) {
    sectionObserver.observe(section);
});



document.getElementById("current-year").textContent = new Date().getFullYear();