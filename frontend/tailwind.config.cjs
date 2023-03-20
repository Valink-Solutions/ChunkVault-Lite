const config = {
	content: ['./src/**/*.{html,js,svelte,ts}'],

	theme: {
		extend: {
			fontFamily: {
				metropolis: ['Metropolis'],
				'metropolis-italic': ['Metropolis-Italic'],
				'metropolis-black': ['Metropolis-Black'],
				'metropolis-black-italic': ['Metropolis-Black-Italic'],
				'metropolis-bold': ['Metropolis-Bold'],
				'metropolis-bold-italic': ['Metropolis-Bold-Italic'],
				'metropolis-semibold': ['Metropolis-SemiBold'],
				'metropolis-semibold-italic': ['Metropolis-SemiBold-Italic'],
				'metropolis-light': ['Metropolis-Light'],
				'metropolis-light-italic': ['Metropolis-Light-Italic']
			},
			dropShadow: {
				neo: '3px 3px 0 black',
				'neo-light': '3px 3px 0 #bdd3f6',
				'neo-pressed': '2px 2px 0 black',
				'neo-card': '6px 6px 0 black'
			},
			borderWidth: {
				2.5: '2.5px',
				3.5: '3.5px'
			}
		}
	},

	plugins: [require('@tailwindcss/typography'), require('daisyui')],

	daisyui: {
		// darkTheme: "mytheme-dark",
		themes: [
			{
				mytheme: {
					primary: '#a855f7',
					secondary: '#60a5fa',
					accent: '#99efa0',
					neutral: '#15151E',
					'base-100': '#f3f4f6',
					info: '#7D93E3',
					success: '#51DBC2',
					warning: '#FBA141',
					error: '#EE1157',
					'--btn': '0.1rem',
					'--padding-card': '1.5rem'
					// "--rounded-box": "1rem", // border radius rounded-box utility class, used in card and other large boxes
					// "--rounded-btn": "0.5rem", // border radius rounded-btn utility class, used in buttons and similar element
					// "--rounded-badge": "1.9rem", // border radius rounded-badge utility class, used in badges and similar
					// "--animation-btn": "0.25s", // duration of animation when you click on button
					// "--animation-input": "0.2s", // duration of animation for inputs like checkbox, toggle, radio, etc
					// "--btn-text-case": "uppercase", // set default text transform for buttons
					// "--btn-focus-scale": "0.95", // scale transform of button when you focus on it
					// "--border-btn": "1px", // border width of buttons
					// "--tab-border": "1px", // border width of tabs
					// "--tab-radius": "0.5rem", // border radius of tabs
				},
				'mytheme-dark': {
					primary: '#a855f7',
					secondary: '#60a5fa',
					accent: '#99efa0',
					neutral: '#15151E',
					'base-100': '#374151',
					info: '#7D93E3',
					success: '#51DBC2',
					warning: '#FBA141',
					error: '#EE1157',
					'--btn': '0.1rem',
					'--padding-card': '1.5rem'
					// "--rounded-box": "1rem", // border radius rounded-box utility class, used in card and other large boxes
					// "--rounded-btn": "0.5rem", // border radius rounded-btn utility class, used in buttons and similar element
					// "--rounded-badge": "1.9rem", // border radius rounded-badge utility class, used in badges and similar
					// "--animation-btn": "0.25s", // duration of animation when you click on button
					// "--animation-input": "0.2s", // duration of animation for inputs like checkbox, toggle, radio, etc
					// "--btn-text-case": "uppercase", // set default text transform for buttons
					// "--btn-focus-scale": "0.95", // scale transform of button when you focus on it
					// "--border-btn": "1px", // border width of buttons
					// "--tab-border": "1px", // border width of tabs
					// "--tab-radius": "0.5rem", // border radius of tabs
				}
			}
		]
	}
};

module.exports = config;
