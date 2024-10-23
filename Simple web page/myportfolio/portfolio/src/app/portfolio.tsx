'use client';

import { useState, useEffect } from 'react';
import { DynamicTitle } from "./assets/dynamic-title.jsx";
import Link from 'next/link';
import { Github, Linkedin, Mail, ArrowUpRight, Sun, Moon, Monitor } from 'lucide-react';
import { ThemeProvider } from './assets/Theme.js';
import useTheme from './assets/Theme.js';
import Image from 'next/image';
import adi from './adi.png';
import SlideTrack from './assets/SlideTrack';

export default function Portfolio() {
  const [activeSection, setActiveSection] = useState('Home');
  const [hoveredSection, setHoveredSection] = useState(null);

  const navItems = ['Home', '|', 'Education', '|', 'Experience', '|', 'Projects', '|', 'Skills', '|', 'Courses', '|', 'Volunteering', '|', 'Contact'];

  useEffect(() => {
    const handleScroll = () => {
      const currentSection = navItems.find((section) => {
        const element = document.getElementById(section.toLowerCase());
        if (element) {
          const rect = element.getBoundingClientRect();
          return rect.top <= 100 && rect.bottom >= 100;
        }
        return false;
      });
      if (currentSection) {
        setActiveSection(currentSection);
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  });

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const ThemeToggle = () => {
    const { thememode, darkmode, lightmode, systemmode } = useTheme();

    return (
      <div className="flex space-x-2">
        <button
          onClick={darkmode}
          aria-label="Enable Dark Mode"
          className={`p-2 rounded-full ${thememode === 'dark' ? 'bg-gray-700 text-white' : 'bg-gray-300 text-black'}`}
        >
          <Moon />
        </button>
        <button
          onClick={lightmode}
          aria-label="Enable Light Mode"
          className={`p-2 rounded-full ${thememode === 'light' ? 'bg-gray-700 text-white' : 'bg-gray-300 text-black'}`}
        >
          <Sun />
        </button>
        <button
          onClick={systemmode}
          aria-label="Enable System Mode"
          className={`p-2 rounded-full ${thememode === 'system' ? 'bg-gray-700 text-white' : 'bg-gray-300 text-black'}`}
        >
          <Monitor />
        </button>
      </div>
    );
  };

  return (
    <ThemeProvider>
      {({ thememode }: { thememode: string }) => (
        <div className={`min-h-screen ${thememode === 'dark' ? 'bg-gray-900 text-white' : 'bg-white text-black'} py-4`}>
          
          {/* Navbar */}
          <nav className="text-lg font-extrabold top-4 mx-auto max-w-fit bg-gray-800 rounded-full px-4 py-2 z-100 flex items-center justify-between">
            <div className="relative flex items-center space-x-1">
              {navItems.map((item) => (
                <button
                  key={item}
                  className={`relative text-white font-medium px-4 py-2 rounded-full z-10 ${activeSection === item ? '' : 'hover:text-white'}`}
                  onMouseEnter={() => setHoveredSection(item)}
                  onMouseLeave={() => setHoveredSection(null)}
                  onClick={() => {
                    const element = document.getElementById(item.toLowerCase());
                    if (element) {
                      element.scrollIntoView({ behavior: 'smooth' });
                    }
                    setActiveSection(item);
                  }}
                >
                  <span className="relative z-20">{item}</span>
                  {hoveredSection === item && (
                    <span
                      className="absolute inset-0 bg-[#FF8C00] rounded-full z-0"
                      style={{ transition: 'all 0.3s ease' }}
                    ></span>
                  )}
                </button>
              ))}
            </div>
            <ThemeToggle />
          </nav>

          <main className="container mx-auto px-4 py-5">
            {/* Profile Section */}
            <section id="home" className="min-h-screen flex items-center">
              <div className="ml-10 grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                <div className="order-2 md:order-1">
                  <h1 className="text-5xl md:text-6xl font-bold mb-4">
                    I&apos;m <span className="text-[#FF8C00]">Adithya S Nair</span>,
                  </h1>

                  <h2 className="text-2xl md:text-4xl font-bold mb-2">
                    <DynamicTitle />
                    <br />
                    AI Undergraduate Student
                  </h2>
                  <div className="mb-6 bg-gray-800 p-4 rounded-lg">
                    <p className="text-1xl font-bold italic">
                      &ldquo;A passionate AI undergraduate student on a mission to drive the development of intelligent analytics solutions. Thriving on challenges and consistently delivering solutions in intense and demanding environments.&rsquo;&rdquo;
                    </p>
                  </div>
                  <div className="flex items-center space-x-4">
                    <Link
                      href="https://github.com/ADITHYASNAIR2021"
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      <button className="text-[#FF8C00] border border-[#FF8C00] hover:bg-[#FF8C00] hover:text-white transition-all duration-300 rounded-full px-6 py-3">
                        Resume
                      </button>
                    </Link>
                    <Link
                      href="https://github.com/ADITHYASNAIR2021"
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      <button className="text-[#FF8C00] border border-[#FF8C00] hover:bg-[#FF8C00] hover:text-white transition-all duration-300 rounded-full px-6 py-3">
                        GitHub
                      </button>
                    </Link>
                    <Link
                      href="https://linkedin.com/in/adithya-s-nair"
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      <button className="text-[#FF8C00] border border-[#FF8C00] hover:bg-[#FF8C00] hover:text-white transition-all duration-300 rounded-full px-6 py-3">
                        LinkedIn
                      </button>
                    </Link>
                  </div>
                </div>
                <div className="order-1 md:order-2 relative">
                  <div className="w-55 h-55 md:w-96 md:h-96 bg-[#FF8C00] rounded-full mx-auto overflow-hidden flex items-center justify-center">
                    <Image
                      src={adi}
                      alt="Adithya S Nair"
                      className="w-full h-full object-contain rounded-full"
                    />
                  </div>
                </div>
              </div>
            </section>

          {/* Education Section */}
          <section id="education" className="py-5">
            <h2 className="text-5xl font-bold mb-8 text-center">Education</h2>
            <div className="space-y-8">
              <div>
                <h3 className="text-xl font-bold">
                  B-Tech, Computer Science with Artificial Intelligence and
                  Machine Learning
                </h3>
                <p className="text-gray-400">
                  Amrita Vishwa Vidyapeetham | 09/2021 – present
                </p>
                <p className="text-gray-400">CGPA: 8.4</p>
              </div>
              <div>
                <h3 className="text-xl font-bold">Higher Secondary (12th)</h3>
                <p className="text-gray-400">
                  Sreyas Public School and Junior College | 03/2019 – 03/2020
                </p>
                <p className="text-gray-400">Percentage: 87%</p>
              </div>
              <div>
                <h3 className="text-xl font-bold">Senior Secondary (10th)</h3>
                <p className="text-gray-400">
                  Sreyas Public School and Junior College | 03/2017 – 03/2018
                </p>
                <p className="text-gray-400">Percentage: 88%</p>
              </div>
            </div>
          </section>

          {/* Professional Experience Section */}
          <section id="experience" className="py-5">
            <h2 className="text-5xl font-bold mb-8 text-center">
              Professional Experience
            </h2>
            <div className="space-y-8">
              <div className="flex">
                <div className="flex flex-col items-center mr-4">
                  <div className="w-4 h-4 rounded-full bg-[#FF8C00]"></div>
                  <div className="w-0.5 h-full bg-gray-700"></div>
                </div>
                <div className="flex-grow bg-gray-800 border border-gray-700 p-6 rounded-lg">
                  <div className="mb-4">
                    <h4 className="text-lg font-semibold">
                      J.P. Morgan Software Engineering Job Simulation
                    </h4>
                    <p className="text-gray-400">07/2024 - 07/2024 | Remote, India</p>
                  </div>
                  <div className="text-gray-400">
                    <ul className="list-disc list-inside">
                      <li>
                        Set up local dev environment and fixed broken files for
                        correct web app output.
                      </li>
                      <li>
                        Used JPMorgan Chase&rsquo;s Perspective library to
                        generate a live data feed graph for traders.
                      </li>
                    </ul>
                  </div>
                </div>
              </div>

              <div className="flex">
                <div className="flex flex-col items-center mr-4">
                  <div className="w-4 h-4 rounded-full bg-[#FF8C00]"></div>
                  <div className="w-0.5 h-full bg-gray-700"></div>
                </div>
                <div className="flex-grow bg-gray-800 border border-gray-700 p-6 rounded-lg">
                  <div className="mb-4">
                    <h4 className="text-lg font-semibold">
                      British Airways Data Science Job Simulation
                    </h4>
                    <p className="text-gray-400">07/2023 - 09/2023 | Remote, India</p>
                  </div>
                  <div className="text-gray-400">
                    <ul className="list-disc list-inside">
                      <li>
                        Scraped and analysed customer review data to uncover
                        findings
                      </li>
                      <li>
                        Built a predictive model to understand factors that
                        influence buying behaviour
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </section>

          {/* Skills Section */}
          <section id="skills" className="py-5">
            <h2 className="text-5xl font-bold mb-8 text-center">Skills</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="bg-gray-800 border border-gray-700 p-6 rounded-lg transform hover:scale-105 transition-transform duration-200">
                <div className="mb-4">
                  <h3 className="text-xl font-bold text-[#FF8C00]">
                    Programming Languages
                  </h3>
                </div>
                <div className="flex flex-wrap gap-2">
                  <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                    Python
                  </span>
                  <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                    Matlab
                  </span>
                  <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                    SQL
                  </span>
                </div>
              </div>
              <div className="bg-gray-800 border border-gray-700 p-6 rounded-lg transform hover:scale-105 transition-transform duration-200">
                <div className="mb-4">
                  <h3 className="text-xl font-bold text-[#FF8C00]">Frameworks</h3>
                </div>
                <div className="flex flex-wrap gap-2">
                  <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                    Django
                  </span>
                  <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                    React
                  </span>
                  <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                    Gradio
                  </span>
                  <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                    Streamlit
                  </span>
                  <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                    Next JS
                  </span>
                  <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                    Tailwind
                  </span>
                  <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                    Node
                  </span>
                </div>
              </div>
              <div className="bg-gray-800 border border-gray-700 p-6 rounded-lg transform hover:scale-105 transition-transform duration-200">
                <div className="mb-4">
                  <h3 className="text-xl font-bold text-[#FF8C00]">AI/ML</h3>
                </div>
                <div className="flex flex-wrap gap-2">
                  <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                    Machine Learning
                  </span>
                  <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                    Deep Learning
                  </span>
                  <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                    Reinforcement Learning
                  </span>
                  <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                    NLP
                  </span>
                  <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                    EDA
                  </span>
                  <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                    LLM
                  </span>
                </div>
              </div>
            </div>
            <SlideTrack />
          </section>

          {/* Projects Section */}
          <section id="projects" className="py-5">
            <h2 className="text-5xl font-bold mb-8 text-center">My Projects</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              <div className="bg-gray-800 border border-gray-700 p-4 rounded-lg flex flex-col justify-between">
                <div>
                  <div className="relative rounded-lg overflow-hidden mb-4">
                    <Image
                      src={adi}
                      alt="Taskify"
                      className="object-cover w-full h-60"
                    />
                  </div>
                  <h3 className="text-2xl font-bold text-[#FF8C00] mb-2">Taskify</h3>
                  <p className="text-gray-400 mb-4">
                    Task manager to keep track of your goals.
                  </p>
                </div>
                <div className="flex justify-between items-center">
                  <div className="flex space-x-2">
                    <span className="text-2xl">🛠️</span>
                    <span className="text-2xl">⚛️</span>
                  </div>
                  <Link
                    href="https://github.com/your-repo"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-white hover:text-gray-300"
                  >
                    <Github size={24} />
                  </Link>
                </div>
              </div>

              <div className="bg-gray-800 border border-gray-700 p-4 rounded-lg flex flex-col justify-between">
                <div>
                  <div className="relative rounded-lg overflow-hidden mb-4">
                    <Image
                      src={adi}
                      alt="Chatiko"
                      className="object-cover w-full h-60"
                    />
                  </div>
                  <h3 className="text-2xl font-bold text-[#FF8C00] mb-2">Chatiko</h3>
                  <p className="text-gray-400 mb-4">Realtime chat app.</p>
                </div>
                <div className="flex justify-between items-center">
                  <div className="flex space-x-2">
                    <span className="text-2xl">💬</span>
                    <span className="text-2xl">⚛️</span>
                  </div>
                  <Link
                    href="https://github.com/your-repo"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-white hover:text-gray-300"
                  >
                    <Github size={24} />
                  </Link>
                </div>
              </div>
            </div>
          </section>

          {/* Community Outreach Section */}
          <section id="community" className="py-5">
            <h2 className="text-5xl font-bold mb-8 text-center">
              Community Outreach
            </h2>
            <div className="bg-gray-800 border border-gray-700 p-6 rounded-lg">
              <div className="mb-4">
                <h3 className="text-xl font-bold text-[#FF8C00]">
                  Student Social Responsibility Project
                </h3>
              </div>
              <p className="mb-4 text-1xl font-bold text-gray-400">
                Conducted a class on Introduction to AI and an awareness campaign
                titled &apos;Decoding AI&apos; at Sreyas Public School, Ponkunnam,
                Kottayam, addressing the objective of AI awareness gap and
                fostering equitable access to AI knowledge and opportunities.
              </p>
            </div>
          </section>

          {/* Courses Section */}
          <section id="courses" className="py-5">
            <h2 className="text-5xl font-bold mb-8 text-center">Courses</h2>
            <div className="bg-gray-800 border border-gray-700 p-6 rounded-lg">
              <p className="text-2xl mb-8 text-center">Relevant Course Work:</p>
              <div className="flex flex-wrap gap-2">
                <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                  DAA
                </span>
                <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                  DSA
                </span>
                <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                  OS
                </span>
                <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                  Advanced Computer Networks
                </span>
                <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                  MIS
                </span>
                <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                  IBS
                </span>
                <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                  Signals and Image Processing
                </span>
                <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                  Python for Machine Learning
                </span>
                <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                  ROS
                </span>
                <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                  RL
                </span>
                <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                  AI in Speech Processing
                </span>
                <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                  NLP
                </span>
                <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                  DL
                </span>
                <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                  DRL
                </span>
                <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                  FSD
                </span>
              </div>
            </div>
          </section>

          {/* Volunteering Section */}
          <section id="volunteering" className="py-5">
            <h2 className="text-5xl font-bold mb-8 text-center">Volunteering</h2>
            <div className="bg-gray-800 border border-gray-700 p-6 rounded-lg">
              <div className="mb-4">
                <h3 className="text-xl font-bold text-[#FF8C00]">Vidyut</h3>
              </div>
              <p className="mb-4 text-1xl font-bold text-gray-400">
                Core committee member &apos;24 and Executive member 2023. My duty
                involved managing accommodation arrangements for participants,
                ensuring their comfort, coordinating with hostels, organizing
                check-ins, and addressing concerns.
              </p>
              <div className="mb-4">
                <h3 className="text-xl font-bold text-[#FF8C00]">ICPC</h3>
              </div>
              <p className="text-1xl font-bold text-gray-400">
                Asia West Regional Finals &apos;22 and 2023. Overall Coordinator,
                assisted in organizing and running the Competition, this
                experience helped me develop strong organizational and
                communication skills while gaining valuable insights into event
                management.
              </p>
            </div>
          </section>

          {/* Languages Section */}
          <section id="languages" className="py-5">
            <h2 className="text-5xl font-bold mb-8 text-center">Languages</h2>
            <div className="flex flex-wrap gap-4 justify-center">
              <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                English (Professional proficiency)
              </span>
              <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                Malayalam (Native proficiency)
              </span>
              <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                Hindi (Working proficiency)
              </span>
              <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                German (Learning)
              </span>
            </div>
          </section>

          {/* Interests Section */}
          <section id="interests" className="py-5">
            <h2 className="text-5xl font-bold mb-8 text-center">Interests</h2>
            <div className="flex flex-wrap gap-4 justify-center">
              <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                Artificial intelligence
              </span>
              <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                Predictive Analysis
              </span>
              <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                Data Analysis
              </span>
              <span className="bg-gray-700 text-white px-3 py-1 rounded-full text-1xl font-bold">
                Singing
              </span>
            </div>
          </section>

          {/* Contact Section */}
          <section id="contact" className="py-5">
            <div className="max-w-2xl mx-auto">
              <h2 className="text-5xl font-bold mb-8 text-center">Contact Me</h2>
              <div className="bg-gray-800 border border-gray-700 p-6 rounded-lg">
                <p className="mb-4 text-gray-400">
                  Feel free to reach out to me for any inquiries or collaboration opportunities.
                </p>
                <ul className="space-y-4">
                  <li className="flex items-center">
                    <Mail className="text-[#FF8C00] mr-2" />
                    <strong className="text-[#FF8C00]">Email:</strong>
                    <span className="ml-2">adithyasnair2021@gmail.com</span>
                  </li>
                  <li className="flex items-center">
                    <span className="text-[#FF8C00] mr-2">📞</span>
                    <strong className="text-[#FF8C00]">Phone:</strong>
                    <span className="ml-2">+91 8136859455</span>
                  </li>
                  <li className="flex items-center">
                    <Linkedin className="text-[#FF8C00] mr-2" />
                    <strong className="text-[#FF8C00]">LinkedIn:</strong>
                    <Link
                      href="https://linkedin.com/in/adithya-s-nair"
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-blue-400 hover:underline ml-2"
                    >
                      linkedin.com/in/adithya-s-nair
                    </Link>
                  </li>
                  <li className="flex items-center">
                    <Github className="text-[#FF8C00] mr-2" />
                    <strong className="text-[#FF8C00]">GitHub:</strong>
                    <Link
                      href="https://github.com/ADITHYASNAIR2021"
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-blue-400 hover:underline ml-2"
                    >
                      github.com/ADITHYASNAIR2021
                    </Link>
                  </li>
                </ul>
              </div>
            </div>
          </section>

          {/* Scroll to Top Button */}
          <button
            className="fixed bottom-4 right-4 bg-[#FF8C00] text-white p-3 rounded-full shadow-lg hover:bg-orange-600 transition duration-300"
            onClick={scrollToTop}
          >
            <ArrowUpRight />
          </button>

          {/* Footer */}
          <footer className="py-8 text-center text-gray-400">
              <p>&copy; 2024 Adithya S Nair. All rights reserved.</p>
            </footer>

          </main>
        </div>
      )}
    </ThemeProvider>
  );
}