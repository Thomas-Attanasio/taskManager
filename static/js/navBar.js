export const displayNavBar = () => {
    const navBarContainer = document.getElementById('navBarContainer');

    navBarContainer.innerHTML = `
        <ul>
            <hr>

            <li>
                <a class="navBarLink" href="/">Your Tasks</a>
            </li>

            <hr>
        </ul>
    `;


    const currentPath = window.location.pathname;
    const links = document.querySelectorAll('.navBarLink');

    links.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
}