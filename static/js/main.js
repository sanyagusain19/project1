
/* ===================================
   GLOBAL PAGE INITIALIZATION
=================================== */

document.addEventListener("DOMContentLoaded", () => {

    console.log("Main JS loaded 🚀");

    /* ===============================
       PAGE ENTER ANIMATION
    =============================== */

    document.body.classList.add("page-enter");


    /* ===============================
       SMOOTH LINK HANDLING (OPTIONAL)
    =============================== */

    const links = document.querySelectorAll("a");

    links.forEach(link => {

        // ignore external links or anchors
        if (
            link.target === "_blank" ||
            link.href.includes("#")
        ) return;

        link.addEventListener("click", (e) => {

            const href = link.getAttribute("href");

            // ignore flask/static/js/css links
            if (!href || href.startsWith("http")) return;

            e.preventDefault();

            // optional exit animation (future upgrade)
            document.body.style.opacity = "0";
            document.body.style.transform = "translateY(10px)";
            document.body.style.transition = "0.3s ease";

            setTimeout(() => {
                window.location.href = href;
            }, 250);
        });

    });

});