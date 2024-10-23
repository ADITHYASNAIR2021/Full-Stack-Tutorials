/** @type {import('next').NextConfig} */
const nextConfig = {
    images: {
      remotePatterns: [
        {
          protocol: 'https',
          hostname: 'skillicons.dev',
          pathname: '/icons',
        },
      ],
      dangerouslyAllowSVG: true, // Allow SVG images
    },
    // You can add more Next.js configurations here as needed
  };
  
  export default nextConfig;
  