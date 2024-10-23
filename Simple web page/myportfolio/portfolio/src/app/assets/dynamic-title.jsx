"use client";
import { Typography } from "./Typography";
import { useEffect, useState } from "react";

export function DynamicTitle() {
  const [title, setTitle] = useState("AI Student");

  useEffect(() => {
    const loop = () => {
      const randomIndex = Math.floor(Math.random() * titles.length);
      const delay = Math.floor(Math.random() * 4000) + 5000;
      setTitle(titles[randomIndex]);
      if (delay > 4100) {
        setTitle(cryptic);
        setTimeout(() => setTitle(titles[randomIndex]), 250); // increased duration
        setTimeout(() => setTitle(cryptic), 500); // increased duration
        setTimeout(() => setTitle(titles[randomIndex]), 750); // increased duration
      }
      setTimeout(loop, delay);
    };
    setTimeout(loop, 1500);
  }, []);

  return (
    <Typography
      variant="h1"
      className="!text-white -ml-2 max-w-[450px] lg:!text-[53px] showTitle"
    >
      {title}
    </Typography>
  );
}

const titles = [
  "AI Student",
  "Data Analyst",
  "Creative Ghost",
  "Frontend Dev.",
  "Software Eng.",
  "AI Student",
  "Creative Ghost",
  "AI Student",
];
const cryptic = "⎍⎎⎒⌭⌿⎎⍅⎎⌿⌶";
