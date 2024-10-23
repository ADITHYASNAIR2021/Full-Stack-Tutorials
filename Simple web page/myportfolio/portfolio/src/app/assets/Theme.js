import React, { createContext, useContext, useState, useEffect } from 'react';

// Create a Theme Context
export const ThemeContext = createContext({
    thememode: "dark",
    mode: true,
    darkmode: () => {},
    lightmode: () => {},
    systemmode: () => {}
});

// Create a Theme Provider component
export const ThemeProvider = ({ children }) => {
    const [thememode, setThemeMode] = useState("dark");
    
    // Function to enable dark mode
    const darkmode = () => {
        setThemeMode("dark");
        localStorage.setItem("theme", "dark");
    };

    // Function to enable light mode
    const lightmode = () => {
        setThemeMode("light");
        localStorage.setItem("theme", "light");
    };

    // Function to enable system mode
    const systemmode = () => {
        setThemeMode("system");
        localStorage.removeItem("theme");
    };

    // Load the saved theme from localStorage on initial render
    useEffect(() => {
        const savedTheme = localStorage.getItem("theme") || "system";
        setThemeMode(savedTheme);
    }, []);

    return (
        <ThemeContext.Provider value={{ thememode, darkmode, lightmode, systemmode }}>
            {children}
        </ThemeContext.Provider>
    );
};

// Custom hook to use the Theme Context
export default function useTheme() {
    return useContext(ThemeContext);
}
