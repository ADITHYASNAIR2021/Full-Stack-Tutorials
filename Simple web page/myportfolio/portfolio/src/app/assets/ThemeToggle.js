import React from 'react';
import useTheme from './Theme.js';

const ThemeToggle = () => {
    const { thememode, darkmode, lightmode, systemmode } = useTheme();

    return (
        <div>
            <p>Current Theme: {thememode}</p>
            <button onClick={darkmode} aria-label="Enable Dark Mode">Dark Mode</button>
            <button onClick={lightmode} aria-label="Enable Light Mode">Light Mode</button>
            <button onClick={systemmode} aria-label="Enable System Mode">System Mode</button>
        </div>
    );
};

export default ThemeToggle;
