<template>
  <div class="min-h-screen bg-slate-950 text-slate-100 font-display select-none">
    <!-- Navigation -->
    <nav class="navbar fixed top-0 left-0 w-full z-50 bg-slate-950/90 backdrop-blur-xl border-b border-slate-800 shadow-lg shadow-black/20">
      <div class="container mx-auto flex justify-between items-center py-4 px-6 lg:px-8 max-w-7xl">
        <div class="nav-brand flex items-center gap-3">
          <div class="w-8 h-8 rounded-full border-2 border-primary flex items-center justify-center bg-primary/10 text-primary font-bold">⟪•⟫</div>
          <span class="font-semibold"> JC Porcopio</span>
        </div>

        <button class="nav-toggle md:hidden flex flex-col justify-between w-[30px] h-[21px] bg-transparent border-none cursor-pointer z-50" aria-label="Toggle navigation" @click="toggleNav">
          <span class="w-full h-[3px] bg-text-main rounded-full transition-all" :class="{ 'rotate-45 translate-y-2': mobileNavOpen, '-rotate-45': mobileNavOpen }"></span>
          <span class="w-full h-[3px] bg-text-main rounded-full transition-all" :class="{ 'opacity-0': mobileNavOpen }"></span>
          <span class="w-full h-[3px] bg-text-main rounded-full transition-all" :class="{ '-rotate-45 -translate-y-2': mobileNavOpen, 'rotate-45': mobileNavOpen }"></span>
        </button>
        
        <ul class="nav-menu flex gap-8 list-none" :class="{ 'active': mobileNavOpen }">
        <li><a href="#home" class="nav-link" :class="{ 'active-link': activeSection === 'home' }" @click="setActiveSection('home'); closeNav()">Home</a></li>
        <li><a href="#about" class="nav-link" :class="{ 'active-link': activeSection === 'about' }" @click="setActiveSection('about'); closeNav()">About</a></li>
        <li><a href="#skills" class="nav-link" :class="{ 'active-link': activeSection === 'skills' }" @click="setActiveSection('skills'); closeNav()">Skills</a></li>
        <li><a href="#projects" class="nav-link" :class="{ 'active-link': activeSection === 'projects' }" @click="setActiveSection('projects'); closeNav()">Projects</a></li>
        <li><a href="#experience" class="nav-link" :class="{ 'active-link': activeSection === 'experience' }" @click="setActiveSection('experience'); closeNav()">Experience</a></li>
        <!-- <li><a href="#certificates" class="nav-link" :class="{ 'active-link': activeSection === 'certificates' }" @click="setActiveSection('certificates'); closeNav()">Certificates</a></li> -->
        <li><a href="#contact" class="nav-link" :class="{ 'active-link': activeSection === 'contact' }" @click="setActiveSection('contact'); closeNav()">Contact</a></li>
        </ul>
      </div>
    </nav>

    <!-- Hero Section (Home) -->
    <main id="home" class="flex-grow flex flex-col relative pt-24 md:pt-32">
      <div class="absolute inset-0 overflow-hidden pointer-events-none">
        <div class="absolute -top-[20%] -right-[10%] w-[600px] h-[600px] rounded-full bg-primary/5 blur-[120px]"></div>
        <div class="absolute top-[40%] -left-[10%] w-[400px] h-[400px] rounded-full bg-purple-500/5 blur-[100px]"></div>
      </div>
      
      <div class="relative mx-auto max-w-7xl flex-1 flex flex-col justify-center px-4 py-12 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 gap-12 lg:grid-cols-2 lg:gap-8 items-center">
          <!-- Text Content -->
          <div class="flex flex-col justify-center text-left">
            <div class="mb-4 inline-flex items-center gap-2 self-start rounded-full border border-primary/20 bg-primary/10 px-3 py-1 text-xs font-medium text-primary">
              <span class="relative flex h-2 w-2">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-primary opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2 w-2 bg-primary"></span>
              </span>
              Available for hire
            </div>
            
            <h1 class="mb-6 text-4xl font-extrabold tracking-tight text-white sm:text-5xl lg:text-6xl">
              John Carl <span class="text-primary">C</span>. <br/>
              Porcopio
            </h1>
            
            <h2 class="mb-8 max-w-2xl text-lg text-text-secondary sm:text-xl leading-relaxed">
              A Junior Web Developer and Mobile IT Student passionate about Python, MySQL, UI/UX, and clean code. I transform ideas into seamless, modern web applications.
            </h2>
            
            <div class="flex flex-wrap gap-4">
                <a href="#projects">
                    <button class="flex items-center justify-center gap-2 rounded-lg bg-primary px-8 py-3 text-base font-bold text-white transition-all hover:bg-primary/90 hover:shadow-[0_0_20px_rgba(19,127,236,0.4)]">
                    <span class="material-symbols-outlined text-[20px]">🚀</span>
                    View Projects
                    </button>
                </a>
                <button @click="openResumeModal" class="flex items-center justify-center gap-2 rounded-lg border border-white/20 bg-transparent px-8 py-3 text-base font-bold text-white transition-all hover:border-white/40 hover:bg-white/5">
                    <span class="material-symbols-outlined text-[20px]">👀</span>
                    View Resume
                </button>
            </div>
            
            <div class="mt-12 flex items-center gap-6">
              <a aria-label="GitHub" class="text-text-secondary transition-colors hover:text-primary" href="https://github.com/KallY-Py" target="_blank">
                <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2C6.48 2 2 6.48 2 12c0 4.42 2.87 8.17 6.84 9.49.5.09.68-.21.68-.48 0-.24-.01-.88-.01-1.72-2.78.6-3.37-1.34-3.37-1.34-.46-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.61.07-.61 1 .07 1.53 1.03 1.53 1.03.89 1.52 2.34 1.08 2.91.83.09-.65.35-1.09.64-1.34-2.22-.25-4.55-1.11-4.55-4.94 0-1.09.39-1.98 1.03-2.68-.1-.25-.45-1.26.1-2.62 0 0 .84-.27 2.75 1.02.8-.22 1.65-.33 2.5-.33.85 0 1.7.11 2.5.33 1.91-1.29 2.75-1.02 2.75-1.02.55 1.36.2 2.37.1 2.62.64.7 1.03 1.59 1.03 2.68 0 3.84-2.34 4.68-4.57 4.93.36.31.68.92.68 1.85 0 1.34-.01 2.42-.01 2.75 0 .27.18.58.69.48A10.02 10.02 0 0 0 22 12c0-5.52-4.48-10-10-10z"/></svg>
              </a>
              <a aria-label="LinkedIn" class="text-text-secondary transition-colors hover:text-primary" href="https://www.linkedin.com/in/porcopio-john-carl-73b93737b/" target="_blank">
                <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C0.792 0 0 0.774 0 1.729v20.542C0 23.227 0.792 24 1.771 24h20.451c0.979 0 1.771-0.773 1.771-1.729V1.729C24 0.774 23.205 0 22.225 0z"/></svg>
              </a>
              <div class="h-px w-12 bg-white/10"></div>
              <span class="text-sm text-text-secondary font-medium">Follow me</span>
            </div>
          </div>
          
          <!-- Visual Code Snippet Card -->
          <div class="relative hidden lg:block">
            <div class="absolute -right-4 -top-4 h-full w-full rounded-2xl bg-gradient-to-br from-primary/20 to-purple-500/20 blur-2xl"></div>
            <div class="relative overflow-hidden rounded-2xl border border-slate-700 bg-slate-900 shadow-2xl">
              <div class="flex items-center gap-2 border-b border-slate-700 bg-slate-800 px-4 py-3">
                <div class="h-3 w-3 rounded-full bg-red-500/80"></div>
                <div class="h-3 w-3 rounded-full bg-yellow-500/80"></div>
                <div class="h-3 w-3 rounded-full bg-green-500/80"></div>
              </div>
              <div class="p-6 font-mono text-sm leading-relaxed">
                <div class="flex gap-4">
                  <div class="flex flex-col text-right text-text-secondary/30 select-none">
                    <span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span><span>8</span><span>9</span><span>10</span><span>11</span>
                  </div>
                  <div class="text-gray-300">
                    <p><span class="text-purple-400">const</span> <span class="text-yellow-300">Developer</span> = {</p>
                    <p class="pl-4">name: <span class="text-green-400">'John Carl C Porcopio'</span>,</p>
                    <p class="pl-4">role: <span class="text-green-400">'Junior Web and Mobile Dev'</span>,</p>
                    <p class="pl-4">skills: [</p>
                    <p class="pl-8"><span class="text-green-400">'Python'</span>, <span class="text-green-400">'PHP'</span>, <span class="text-green-400">'MySQL'</span>, <span class="text-green-400">'UI/UX'</span></p>
                    <p class="pl-4">],</p>
                    <p class="pl-4">hardWorker: <span class="text-blue-400">true</span>,</p>
                    <p class="pl-4">openToWork: <span class="text-blue-400">true</span>,</p>
                    <p class="pl-4">hire: <span class="text-purple-400">function</span>() {</p>
                    <p class="pl-8"><span class="text-purple-400">return</span> <span class="text-green-400">"Let's build together!"</span>;</p>
                    <p class="pl-4">}</p>
                    <p>};</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="absolute -bottom-6 -left-6 rounded-xl border border-slate-700 bg-slate-800/90 p-4 shadow-xl backdrop-blur-md">
              <div class="flex items-center gap-3">
                <div class="rounded-full bg-green-500/20 p-2 text-green-500">
                  <span class="material-symbols-outlined">check_circle</span>
                </div>
                <div>
                  <p class="text-xs text-text-secondary">Status</p>
                  <p class="text-sm font-bold text-white">Seeking Opportunities</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- About Section -->
    <section id="about" class="py-20">
      <div class="container mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <h2 class="text-4xl font-bold mb-10 relative inline-block bg-gradient-to-r from-white to-primary bg-clip-text text-transparent after:content-[''] after:absolute after:bottom-[-10px] after:left-0 after:w-[60px] after:h-[3px] after:bg-primary after:rounded-full">About Me</h2>
        <div class="max-w-3xl space-y-4">
          <p class="text-text-secondary leading-relaxed">I am a passionate IT student nearing the end of my degree, with a strong foundation in modern web technologies. I love building clean, user-friendly interfaces and believe that good design is as important as good code.</p>
          <h3 class="text-xl font-semibold text-primary mt-4">Career Objective</h3>
          <p class="text-text-secondary leading-relaxed">Seeking a Junior Web Developer / IT Support role where I can apply my knowledge in Python, Flask, MySQL, and server management. I am eager to learn from experienced professionals, contribute to the team, and steadily grow my skills while helping deliver reliable and efficient technical solutions.</p>
          <h3 class="text-xl font-semibold text-primary mt-4">Tech Stack Overview</h3>
          <div class="flex flex-wrap gap-2 mt-2">
            <span class="bg-primary/15 px-4 py-2 rounded-full text-sm font-medium border border-primary/30">HTML5</span>
            <span class="bg-primary/15 px-4 py-2 rounded-full text-sm font-medium border border-primary/30">CSS</span>
            <span class="bg-primary/15 px-4 py-2 rounded-full text-sm font-medium border border-primary/30">JavaScript</span>
            <span class="bg-primary/15 px-4 py-2 rounded-full text-sm font-medium border border-primary/30">Dart</span>
            <span class="bg-primary/15 px-4 py-2 rounded-full text-sm font-medium border border-primary/30">PHP</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="py-20 bg-slate-900">
      <div class="container mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <h2 class="text-4xl font-bold mb-10 relative inline-block bg-gradient-to-r from-white to-primary bg-clip-text text-transparent after:content-[''] after:absolute after:bottom-[-10px] after:left-0 after:w-[60px] after:h-[3px] after:bg-primary after:rounded-full">Skills</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mt-4">
          <div class="bg-slate-800/70 backdrop-blur-md rounded-xl p-6 border border-slate-700 shadow-lg">
            <h3 class="text-xl font-semibold text-primary mb-4">Frontend</h3>
            <div class="flex flex-wrap gap-2"><span class="bg-primary/10 px-3 py-1 rounded-full text-sm">HTML</span><span class="bg-primary/10 px-3 py-1 rounded-full text-sm">CSS</span><span class="bg-primary/10 px-3 py-1 rounded-full text-sm">JavaScript</span><span class="bg-primary/10 px-3 py-1 rounded-full text-sm">Tailwind CSS</span></div>
          </div>
          <div class="bg-slate-800/70 backdrop-blur-md rounded-xl p-6 border border-slate-700 shadow-lg">
            <h3 class="text-xl font-semibold text-primary mb-4">Backend</h3>
            <div class="flex flex-wrap gap-2"><span class="bg-primary/10 px-3 py-1 rounded-full text-sm">Python</span><span class="bg-primary/10 px-3 py-1 rounded-full text-sm">PHP</span><span class="bg-primary/10 px-3 py-1 rounded-full text-sm">MySQL</span><span class="bg-primary/10 px-3 py-1 rounded-full text-sm">Firebase</span></div>
          </div>
          <div class="bg-slate-800/70 backdrop-blur-md rounded-xl p-6 border border-slate-700 shadow-lg">
            <h3 class="text-xl font-semibold text-primary mb-4">Mobile</h3>
            <div class="flex flex-wrap gap-2"><span class="bg-primary/10 px-3 py-1 rounded-full text-sm">Flutter</span><span class="bg-primary/10 px-3 py-1 rounded-full text-sm">Responsive Design</span><span class="bg-primary/10 px-3 py-1 rounded-full text-sm">Dart</span></div>
          </div>
          <div class="bg-slate-800/70 backdrop-blur-md rounded-xl p-6 border border-slate-700 shadow-lg">
            <h3 class="text-xl font-semibold text-primary mb-4">Tools & Others</h3>
            <div class="flex flex-wrap gap-2"><span class="bg-primary/10 px-3 py-1 rounded-full text-sm">GitHub</span><span class="bg-primary/10 px-3 py-1 rounded-full text-sm">VS Code</span><span class="bg-primary/10 px-3 py-1 rounded-full text-sm">Figma</span></div>
          </div>
        </div>
      </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="py-20">
      <div class="container mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <h2 class="text-4xl font-bold mb-10 relative inline-block bg-gradient-to-r from-white to-primary bg-clip-text text-transparent after:content-[''] after:absolute after:bottom-[-10px] after:left-0 after:w-[60px] after:h-[3px] after:bg-primary after:rounded-full">Projects</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div class="bg-slate-800/70 backdrop-blur-md rounded-xl overflow-hidden border border-slate-700 hover:border-primary hover:shadow-[0_0_30px_rgba(59,130,246,0.25)] transition-all duration-300 hover:-translate-y-2">
            <div class="h-48 bg-gradient-to-r from-gray-800 to-gray-900 flex items-center justify-center text-5xl">🛒</div>
            <div class="p-6"><h3 class="text-xl font-bold mb-2">Web & Mobile E-Commerce Platform</h3><p class="text-text-secondary text-sm mb-4">Full-stack shopping platform with authentication, product management, cart functionality.</p><div class="flex flex-wrap gap-2 mb-4"><span class="bg-slate-700 px-3 py-1 rounded-full text-xs">Flutter</span><span class="bg-slate-700 px-3 py-1 rounded-full text-xs">Dart</span><span class="bg-slate-700 px-3 py-1 rounded-full text-xs">MySQL</span></div><div class="flex gap-4"><a href="https://github.com/KallY-Py/Ecommerce" target="_blank" class="text-text-secondary hover:text-primary text-sm">🔗 GitHub</a></div></div>
          </div>
          <div class="bg-slate-800/70 backdrop-blur-md rounded-xl overflow-hidden border border-slate-700 hover:border-primary hover:shadow-[0_0_30px_rgba(59,130,246,0.25)] transition-all duration-300 hover:-translate-y-2">
            <div class="h-48 bg-gradient-to-r from-gray-800 to-gray-900 flex items-center justify-center text-5xl">🎓</div>
            <div class="p-6"><h3 class="text-xl font-bold mb-2">LSEF TESDA Blockchain Portal</h3><p class="text-text-secondary text-sm mb-4">Student portal with blockchain certificate verification, secure credentials.</p><div class="flex flex-wrap gap-2 mb-4"><span class="bg-slate-700 px-3 py-1 rounded-full text-xs">Python</span><span class="bg-slate-700 px-3 py-1 rounded-full text-xs">Flask</span><span class="bg-slate-700 px-3 py-1 rounded-full text-xs">MySQL</span></div><div class="flex gap-4"><a href="#" class="text-text-secondary hover:text-primary text-sm">🔗 GitHub</a></div></div>
          </div>
          <div class="bg-slate-800/70 backdrop-blur-md rounded-xl overflow-hidden border border-slate-700 hover:border-primary hover:shadow-[0_0_30px_rgba(59,130,246,0.25)] transition-all duration-300 hover:-translate-y-2">
            <div class="h-48 bg-gradient-to-r from-gray-800 to-gray-900 flex items-center justify-center text-5xl">🎮</div>
            <div class="p-6"><h3 class="text-xl font-bold mb-2">Simple Python Web Games</h3><p class="text-text-secondary text-sm mb-4">Number Guessing, Tic-Tac-Toe, Memory Card Game with Flask backend.</p><div class="flex flex-wrap gap-2 mb-4"><span class="bg-slate-700 px-3 py-1 rounded-full text-xs">Python</span><span class="bg-slate-700 px-3 py-1 rounded-full text-xs">JavaScript</span><span class="bg-slate-700 px-3 py-1 rounded-full text-xs">CSS</span></div><div class="flex gap-4"><a href="#" class="text-text-secondary hover:text-primary text-sm">🔗 GitHub</a></div></div>
          </div>
        </div>
      </div>
    </section>

    <!-- Experience & Education Section -->
    <section id="experience" class="py-20 bg-slate-900">
      <div class="container mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <h2 class="text-4xl font-bold mb-10 relative inline-block bg-gradient-to-r from-white to-primary bg-clip-text text-transparent after:content-[''] after:absolute after:bottom-[-10px] after:left-0 after:w-[60px] after:h-[3px] after:bg-primary after:rounded-full">Experience & Education</h2>
        <div class="space-y-8">
          <div class="flex gap-4"><div class="w-3 h-3 bg-primary rounded-full mt-2 shadow-[0_0_0_3px_rgba(19,127,236,0.2)]"></div><div class="flex-1 border-l border-white/10 pl-6 pb-4"><h3 class="text-xl font-semibold">Bachelor of Science in Information Technology</h3><p class="text-primary text-sm mt-1">Laguna State Polytechnic University – Santa Cruz Campus | 2022 - Present</p><p class="text-text-secondary mt-2">Pursuing IT with focus on web/mobile development, database management, strong academic record.</p></div></div>
          <div class="flex gap-4"><div class="w-3 h-3 bg-primary rounded-full mt-2 shadow-[0_0_0_3px_rgba(19,127,236,0.2)]"></div><div class="flex-1 border-l border-white/10 pl-6 pb-4"><h3 class="text-xl font-semibold">Seeking OJT Position</h3><p class="text-primary text-sm mt-1">Junior Web Development / IT Support | 2025</p><p class="text-text-secondary mt-2">Looking for On-the-Job Training to apply academic knowledge, contribute to real-world projects.</p></div></div>
        </div>
      </div>
    </section>

    <!-- Certificates Section -->
    <section id="certificates" class="py-20">
      <div class="container mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <h2 class="text-4xl font-bold mb-10 relative inline-block bg-gradient-to-r from-white to-primary bg-clip-text text-transparent after:content-[''] after:absolute after:bottom-[-10px] after:left-0 after:w-[60px] after:h-[3px] after:bg-primary after:rounded-full">Certifications</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- IT Specialist Certificate -->
          <!-- <div class="bg-slate-800/70 backdrop-blur-md rounded-xl overflow-hidden border border-slate-700 hover:border-primary hover:shadow-[0_0_30px_rgba(59,130,246,0.25)] transition-all duration-300 hover:-translate-y-2 cursor-pointer" @click="openCertificateModal('it')">
            <div class="p-6 flex flex-col items-center text-center">
              <img src="@/assets/itbadge.png" alt="IT Specialist" class="w-24 h-24 object-contain mb-4">
              <h3 class="text-xl font-bold mb-2">IT Specialist - Artificial Intelligence</h3>
              <p class="text-primary text-sm mb-1">Certiport, a Pearson VUE business</p>
              <p class="text-text-secondary text-xs">Expires May 14, 2031</p>
            </div>
          </div> -->

          <!-- Linux Essentials Certificate -->
          <div class="bg-slate-800/70 backdrop-blur-md rounded-xl overflow-hidden border border-slate-700 hover:border-primary hover:shadow-[0_0_30px_rgba(59,130,246,0.25)] transition-all duration-300 hover:-translate-y-2 cursor-pointer" @click="openCertificateModal('linux')">
            <div class="p-6 flex flex-col items-center text-center">
              <img src="@/assets/linuxbadge.png" alt="Linux Essentials" class="w-24 h-24 object-contain mb-4">
              <h3 class="text-xl font-bold mb-2">Linux Essentials</h3>
              <p class="text-primary text-sm mb-1">Cisco</p>
              <p class="text-text-secondary text-xs">Issued Dec 7, 2025</p>
            </div>
          </div>

          <!-- Operating Systems Basics Certificate -->
          <div class="bg-slate-800/70 backdrop-blur-md rounded-xl overflow-hidden border border-slate-700 hover:border-primary hover:shadow-[0_0_30px_rgba(59,130,246,0.25)] transition-all duration-300 hover:-translate-y-2 cursor-pointer" @click="openCertificateModal('os')">
            <div class="p-6 flex flex-col items-center text-center">
              <img src="@/assets/osbadge.png" alt="Operating Systems Basics" class="w-24 h-24 object-contain mb-4">
              <h3 class="text-xl font-bold mb-2">Operating Systems Basics</h3>
              <p class="text-primary text-sm mb-1">Cisco</p>
              <p class="text-text-secondary text-xs">Issued Oct 26, 2025</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="py-20 bg-slate-900">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="mb-10 text-center">
          <div class="inline-flex items-center gap-2 px-4 py-2 bg-cyan-500/10 border border-cyan-500/30 rounded-full">
            <span class="relative flex h-2 w-2">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
              <span class="relative inline-flex rounded-full h-2 w-2 bg-green-400"></span>
            </span>
            <span class="text-cyan-400 font-mono text-sm">OPEN FOR OJT / INTERNSHIP OPPORTUNITIES</span>
          </div>
        </div>

        <div class="grid md:grid-cols-2 gap-12">
          <div>
            <div class="bg-[#1a1c23] rounded-xl border border-gray-800 p-6 md:p-8 mb-8">
              <h2 class="text-2xl font-bold text-white mb-4">Let's Work <span class="text-cyan-400">Together</span></h2>
              <p class="text-gray-400 leading-relaxed">
                I'm currently seeking OJT opportunities and open to discussing how I can contribute to your team. 
                Feel free to reach out!
              </p>
            </div>

            <div class="space-y-4">
              <a href="mailto:jcporcopio03@gmail.com" 
                 class="flex items-center gap-4 p-4 bg-[#1a1c23] rounded-xl border border-gray-800 hover:border-cyan-500/50 transition-all duration-300 group hover:-translate-y-1">
                <div class="w-12 h-12 rounded-full bg-gradient-to-r from-cyan-500/20 to-blue-600/20 flex items-center justify-center group-hover:scale-110 transition-transform">
                  <svg class="w-6 h-6 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                  </svg>
                </div>
                <div>
                  <p class="text-gray-500 text-xs font-mono">EMAIL</p>
                  <p class="text-white group-hover:text-cyan-400 transition-colors">jcporcopio03@gmail.com</p>
                </div>
              </a>

              <a href="https://github.com/KallY-Py" target="_blank" rel="noopener noreferrer"
                 class="flex items-center gap-4 p-4 bg-[#1a1c23] rounded-xl border border-gray-800 hover:border-cyan-500/50 transition-all duration-300 group hover:-translate-y-1">
                <div class="w-12 h-12 rounded-full bg-gradient-to-r from-cyan-500/20 to-blue-600/20 flex items-center justify-center group-hover:scale-110 transition-transform">
                  <svg class="w-6 h-6 text-cyan-400" fill="currentColor" viewBox="0 0 24 24">
                    <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"/>
                  </svg>
                </div>
                <div>
                  <p class="text-gray-500 text-xs font-mono">GITHUB</p>
                  <p class="text-white group-hover:text-cyan-400 transition-colors">@KallY-Py</p>
                </div>
              </a>

              <a href="https://www.linkedin.com/in/porcopio-john-carl-73b93737b/" target="_blank" rel="noopener noreferrer"
                 class="flex items-center gap-4 p-4 bg-[#1a1c23] rounded-xl border border-gray-800 hover:border-cyan-500/50 transition-all duration-300 group hover:-translate-y-1">
                <div class="w-12 h-12 rounded-full bg-gradient-to-r from-cyan-500/20 to-blue-600/20 flex items-center justify-center group-hover:scale-110 transition-transform">
                  <svg class="w-6 h-6 text-cyan-400" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451c.979 0 1.771-.773 1.771-1.729V1.729C24 .774 23.204 0 22.225 0z"/>
                  </svg>
                </div>
                <div>
                  <p class="text-gray-500 text-xs font-mono">LINKEDIN</p>
                  <p class="text-white group-hover:text-cyan-400 transition-colors">John Carl Porcopio</p>
                </div>
              </a>
            </div>

            <div class="mt-8 p-4 rounded-lg bg-gradient-to-r from-cyan-500/10 to-blue-600/10 border border-cyan-500/20 text-center">
              <div class="flex items-center justify-center gap-2">
                <span class="relative flex h-2 w-2">
                  <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
                  <span class="relative inline-flex rounded-full h-2 w-2 bg-green-400"></span>
                </span>
                <span class="text-cyan-400 text-sm font-mono">Available for immediate OJT placement</span>
              </div>
            </div>
          </div>

          <div>
            <div class="bg-[#1a1c23] rounded-xl border border-gray-800 p-6 md:p-8">
              <div class="flex items-center gap-2 mb-6 pb-3 border-b border-gray-800">
                <div class="flex gap-1.5">
                  <div class="w-3 h-3 rounded-full bg-red-500/60"></div>
                  <div class="w-3 h-3 rounded-full bg-yellow-500/60"></div>
                  <div class="w-3 h-3 rounded-full bg-green-500/60"></div>
                </div>
              </div>

              <form @submit.prevent="handleSubmit" class="space-y-5">
                <div>
                  <label class="block text-cyan-400 text-sm font-mono mb-2">> NAME</label>
                  <input 
                    v-model="form.name" 
                    type="text" 
                    required
                    placeholder="John Doe"
                    class="w-full px-4 py-3 bg-[#0d0f14] border border-gray-700 rounded-lg focus:outline-none focus:border-cyan-500 text-white placeholder-gray-600 transition-all duration-300"
                  >
                </div>

                <div>
                  <label class="block text-cyan-400 text-sm font-mono mb-2">> EMAIL</label>
                  <input 
                    v-model="form.email" 
                    type="email" 
                    required
                    placeholder="hello@example.com"
                    class="w-full px-4 py-3 bg-[#0d0f14] border border-gray-700 rounded-lg focus:outline-none focus:border-cyan-500 text-white placeholder-gray-600 transition-all duration-300"
                  >
                </div>

                <div>
                  <label class="block text-cyan-400 text-sm font-mono mb-2">> MESSAGE</label>
                  <textarea 
                    v-model="form.message" 
                    rows="5" 
                    required
                    placeholder="Your message here..."
                    class="w-full px-4 py-3 bg-[#0d0f14] border border-gray-700 rounded-lg focus:outline-none focus:border-cyan-500 text-white placeholder-gray-600 resize-none transition-all duration-300"
                  ></textarea>
                </div>

                <button 
                  type="submit" 
                  :disabled="isSubmitting"
                  class="relative w-full group overflow-hidden rounded-lg bg-gradient-to-r from-cyan-500 to-blue-600 text-white py-3 font-semibold transition-all duration-300 transform hover:scale-[1.02] hover:shadow-lg hover:shadow-cyan-500/25 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <span class="relative z-10 flex items-center justify-center gap-2">
                    <span v-if="!isSubmitting">{{ buttonText }}</span>
                    <span v-else class="flex items-center gap-2">
                      <svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                      </svg>
                      Sending...
                    </span>
                  </span>
                  <span class="absolute inset-0 bg-gradient-to-r from-cyan-600 to-blue-700 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></span>
                </button>
              </form>

              <div v-if="showSuccess" class="mt-4 p-3 bg-green-500/10 border border-green-500/30 rounded-lg text-center">
                <p class="text-green-400 text-sm">✓ Message sent successfully! I'll get back to you soon.</p>
              </div>

              <div class="mt-6 pt-4 border-t border-gray-800">
                <p class="text-gray-500 text-xs font-mono text-center">
                  <span class="text-cyan-400">©</span> echo "Message received. Response time: &lt; 24hrs"
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="relative py-16 overflow-hidden bg-[#0a0c10] border-t border-gray-800">
      <div class="absolute inset-0">
        <div class="absolute top-0 left-1/4 w-96 h-96 bg-cyan-500/10 rounded-full blur-[100px]"></div>
        <div class="absolute bottom-0 right-1/4 w-96 h-96 bg-blue-600/10 rounded-full blur-[100px]"></div>
      </div>
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
        <p class="text-gray-400 text-sm">
          Based in Sta. Cruz, Laguna, Philippines — Available for remote or on-site opportunities
        </p>
      </div>
    </section>

    <footer class="bg-slate-950 text-center py-8 border-t border-slate-800">
      <div class="max-w-6xl mx-auto px-4">
      <div class="flex flex-col lg:flex-row justify-between items-center lg:items-start gap-8 mb-8">
        <div class="text-center lg:text-left">
          <h3 class="text-xl font-semibold mb-4 text-blue-400">Contact:</h3>
          <div class="space-y-2">
            <p class="text-gray-300">jcporpopio@gmail.com</p>
            <p class="text-gray-300">09083277282</p>
          </div>
        </div>
        
        <div class="flex space-x-6">
          <a href="https://github.com/" target="_blank" rel="noopener noreferrer" class="text-gray-400 hover:text-white transition duration-200 transform hover:scale-110">
            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
              <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026.8-.223 1.65-.334 2.5-.334.85 0 1.7.111 2.5.334 1.91-1.295 2.75-1.026 2.75-1.026.544 1.378.201 2.397.099 2.65.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" />
            </svg>
          </a>
          <a href="https://linkedin.com/" target="_blank" rel="noopener noreferrer" class="text-gray-400 hover:text-white transition duration-200 transform hover:scale-110">
            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
              <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" />
            </svg>
          </a>
          <a href="https://tiktok.com/" target="_blank" rel="noopener noreferrer" class="text-gray-400 hover:text-white transition duration-200 transform hover:scale-110">
            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
              <path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1-.1z" />
            </svg>
          </a>
          <a href="mailto:jcporpopio@gmail.com" class="text-gray-400 hover:text-white transition duration-200 transform hover:scale-110">
            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
              <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" />
            </svg>
          </a>
          <a href="https://facebook.com/" target="_blank" rel="noopener noreferrer" class="text-gray-400 hover:text-white transition duration-200 transform hover:scale-110">
            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
              <path d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.879v-6.99h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.99C18.343 21.128 22 16.991 22 12z" />
            </svg>
          </a>
        </div>
      </div>
      
      <div class="border-t border-gray-800 my-6"></div>
      
      <div class="flex flex-col md:flex-row justify-between items-center text-sm text-gray-500">
        <p>&copy; {{ currentYear }} JC Porpio. All rights reserved.</p>
        <div class="flex space-x-6 mt-4 md:mt-0">
          <a href="#" class="hover:text-blue-400 transition duration-200">Privacy Policy</a>
          <a href="#" class="hover:text-blue-400 transition duration-200">Terms of Service</a>
        </div>
      </div>
    </div>
    </footer>

    <!-- Certificate Modal -->
    <div v-if="modalVisible" class="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-black/80 backdrop-blur-md" @click="closeModal">
        <div class="relative bg-slate-900 rounded-2xl max-w-4xl w-full max-h-[90vh] overflow-y-auto border border-slate-700 shadow-2xl" @click.stop>
            <div class="sticky top-0 bg-slate-900 border-b border-slate-700 p-4 flex justify-between items-center">
            <h3 class="text-xl font-bold text-white">{{ modalTitle }}</h3>
            <button @click="closeModal" class="text-slate-400 hover:text-white transition text-2xl">&times;</button>
            </div>
            <div class="p-6 flex items-center justify-center">
            <img :src="modalImageUrl" alt="Certificate" class="w-full h-auto rounded-lg shadow-lg">
            </div>
        </div>
    </div>

        <!-- Resume Modal -->
    <div v-if="resumeModalVisible" class="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-black/80 backdrop-blur-md" @click="closeResumeModal">
      <div class="relative bg-slate-900 rounded-2xl max-w-4xl w-full max-h-[90vh] overflow-y-auto border border-slate-700 shadow-2xl" @click.stop>
        <div class="sticky top-0 bg-slate-900 border-b border-slate-700 p-4 flex justify-between items-center">
          <h3 class="text-xl font-bold text-white">My Resume</h3>
          <button @click="closeResumeModal" class="text-slate-400 hover:text-white transition text-2xl">&times;</button>
        </div>
        <div class="p-6 flex items-center justify-center">
          <img :src="resumeImage" alt="Resume" class="w-full h-auto rounded-lg shadow-lg">
        </div>
      </div>
    </div>
</div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'RPGPortfolio',
  setup() {
    const mobileNavOpen = ref(false)
    const form = ref({ name: '', email: '', message: '' })
    const modalVisible = ref(false)
    const modalTitle = ref('')
    const modalImageUrl = ref('')
    const resumeModalVisible = ref(false)
    const resumeImage = ref(require('@/assets/resume.png'))
    const activeSection = ref('home')
    const isSubmitting = ref(false)
    const showSuccess = ref(false)
    const buttonText = ref('Send Message')
    const currentYear = ref(new Date().getFullYear())

    const certificates = {
      it: {
        title: 'IT Specialist - Artificial Intelligence',
        image: require('@/assets/it.png')
      },
      linux: {
        title: 'Linux Essentials',
        image: require('@/assets/linux.png')
      },
      os: {
        title: 'Operating Systems Basics',
        image: require('@/assets/os.png')
      }
    }

    const toggleNav = () => {
      mobileNavOpen.value = !mobileNavOpen.value
    }

    const closeNav = () => {
      mobileNavOpen.value = false
    }

    const openResumeModal = () => {
      resumeModalVisible.value = true
    }

    const closeResumeModal = () => {
      resumeModalVisible.value = false
    }

    const handleSubmit = async () => {
        isSubmitting.value = true
        buttonText.value = 'Sending...'
        
        try {
            const response = await fetch('http://localhost:5000/api/send-message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: form.value.name,
                email: form.value.email,
                message: form.value.message
            })
            })
            
            const result = await response.json()
            
            if (response.ok && result.success) {
            alert(result.message)
            form.value = { name: '', email: '', message: '' }
            
            showSuccess.value = true
            setTimeout(() => {
                showSuccess.value = false
            }, 3000)
            } else {
            alert(result.message || 'Failed to send message. Please try again.')
            }
        } catch (error) {
            console.error('Error sending message:', error)
            alert('Network error. Please check your connection and try again.')
        } finally {
            isSubmitting.value = false
            buttonText.value = 'Send Message'
        }
    }

    const openCertificateModal = (certType) => {
      const cert = certificates[certType]
      if (cert) {
        modalTitle.value = cert.title
        modalImageUrl.value = cert.image
        modalVisible.value = true
      }
    }

    const closeModal = () => {
      modalVisible.value = false
      modalTitle.value = ''
      modalImageUrl.value = ''
    }

    const setActiveSection = (section) => {
      activeSection.value = section
    }

    const handleScroll = () => {
      const sections = ['home', 'about', 'skills', 'projects', 'experience', 'certificates', 'contact']
      const scrollPosition = window.scrollY + 100
    
      for (const section of sections) {
        const element = document.getElementById(section)
        if (element) {
          const offsetTop = element.offsetTop
          const offsetBottom = offsetTop + element.offsetHeight
          
          if (scrollPosition >= offsetTop && scrollPosition < offsetBottom) {
            activeSection.value = section
            break
          }
        }
      }
    }

    document.addEventListener('copy', (e) => {
      e.preventDefault()
      return false
    })
    
    document.addEventListener('cut', (e) => {
      e.preventDefault()
      return false
    })
    
    document.addEventListener('paste', (e) => {
      e.preventDefault()
      return false
    })
    
    document.addEventListener('contextmenu', (e) => {
      e.preventDefault()
      return false
    })

    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && (e.key === 'c' || e.key === 'C' || e.key === 'v' || e.key === 'V' || e.key === 'x' || e.key === 'X')) {
        e.preventDefault()
        return false
      }
    })

    window.addEventListener('scroll', handleScroll)
    
    handleScroll()

    return {
      mobileNavOpen,
      form,
      modalVisible,
      modalTitle,
      modalImageUrl,
      resumeModalVisible,
      resumeImage,
      activeSection,
      isSubmitting,
      showSuccess,
      buttonText,
      currentYear,
      toggleNav,
      closeNav,
      openResumeModal,
      closeResumeModal,
      handleSubmit,
      openCertificateModal,
      closeModal,
      setActiveSection,
      handleScroll
    }
  }
}
</script>

<style scoped>
.nav-menu {
  transition: all 0.3s ease;
}

@media (max-width: 768px) {
  .nav-menu {
    position: fixed;
    left: -100%;
    top: 70px;
    flex-direction: column;
    background-color: rgba(15, 23, 42, 0.95);
    backdrop-filter: blur(8px);
    width: 100%;
    text-align: center;
    padding: 2rem 0;
    gap: 1.5rem;
    z-index: 40;
  }
  
  .nav-menu.active {
    left: 0;
  }
}

.nav-link {
  transition: color 0.2s;
}

.nav-link:hover {
  color: #137fec;
}

@keyframes ping {
  75%, 100% {
    transform: scale(2);
    opacity: 0;
  }
}

.animate-ping {
  animation: ping 1s cubic-bezier(0, 0, 0.2, 1) infinite;
}

html {
  scroll-behavior: smooth;
}

.glass-card {
  background: rgba(30, 41, 59, 0.7);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(148, 163, 184, 0.15);
}

.section-title {
  color: #f8fafc;
}

.text-muted {
  color: #cbd5e1;
}

* {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.nav-link.active-link {
  color: #137fec;
  position: relative;
}

.nav-link.active-link::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 0;
  width: 100%;
  height: 2px;
  background: #137fec;
  border-radius: 2px;
}

@media (max-width: 768px) {
  .nav-link.active-link::after {
    bottom: -4px;
  }
}
</style>