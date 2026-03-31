export const displayNavBar = () => {
    const navBarContainer = document.getElementById('navBarContainer');

    navBarContainer.innerHTML = `
        <ul>
            <hr>

            <li>
                <a class="navBarLink" href="/">Home</a>
            </li>

            <hr>
        </ul>
    `;
}