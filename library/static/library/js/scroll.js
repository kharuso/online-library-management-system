var navBar = document.getElementById("navbar");
			window.onscroll = function () {
				if (window.scrollY) {
					navBar.classList.add("scrolled");
				} else {
					navBar.classList.remove("scrolled");
				}
			};