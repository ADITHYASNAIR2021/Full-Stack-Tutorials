import React from 'react';
import Image from 'next/image';

function SlideTrack() {
    const images = [
        "html",
        "css",
        "js",
        "python",
        "react",
        "tailwind",
        "nodejs",
        "mongodb",
        "express",
        "firebase",
        "appwrite",
        "vscode",
        "git",
        "aws",
    ];

    return (
        <div id="logos" className="overflow-hidden flex py-10 px-0">
            <div id="logo-slider1" className="whitespace-nowrap animate-slide space-x-10 hover:[animation-play-state:paused]">
                {images.map((src, index) => (
                    <div key={index} className="inline-block">
                        <Image 
                            src={`https://skillicons.dev/icons?i=${src}`} 
                            alt={`${src} icon`} 
                            width={80} 
                            height={80} 
                            className="hover:scale-125 transition-transform duration-300" 
                            title={src.toUpperCase()} 
                        />
                    </div>
                ))}
            </div>
        </div>
    );
}

export default SlideTrack;
