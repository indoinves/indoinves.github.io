#!/usr/bin/env python3
import os

AI_CATEGORIES = [
    {"slug": "chatbots-llm", "name": "AI Chatbots & LLM", "desc": "Conversational AI and Large Language Models."},
    {"slug": "image-generation", "name": "AI Image Generators", "desc": "Text-to-image and visual art creation tools."},
    {"slug": "code-assistant", "name": "AI Code Assistants", "desc": "Programming, debugging, and software development AI."},
    {"slug": "video-creation", "name": "AI Video Creators", "desc": "Synthetic video generation and editing tools."},
    {"slug": "audio-voice", "name": "AI Audio & Voice", "desc": "Text-to-speech, voice cloning, and audio enhancement."},
    {"slug": "seo-marketing", "name": "AI SEO & Marketing", "desc": "Content optimization, ranking, and digital marketing."},
    {"slug": "copywriting", "name": "AI Copywriting", "desc": "Blog posts, ad copy, and social media captions."},
    {"slug": "data-analytics", "name": "AI Data Analytics", "desc": "Business intelligence, forecasting, and data visualization."},
    {"slug": "productivity", "name": "AI Productivity Tools", "desc": "Task automation, summarization, and note-taking."},
    {"slug": "translation", "name": "AI Translation & Localization", "desc": "Multilingual translation and voice localization."},
    {"slug": "presentation", "name": "AI Presentation Makers", "desc": "Slide decks, pitch books, and infographics generator."},
    {"slug": "legal-assistant", "name": "AI Legal Assistants", "desc": "Contract review, compliance checking, and legal research."},
    {"slug": "finance-crypto", "name": "AI Finance & Crypto", "desc": "Algorithmic trading, portfolio tracking, and market analysis."},
    {"slug": "education-tutor", "name": "AI Education & Tutoring", "desc": "Personalized learning, quiz generators, and academic tools."},
    {"slug": "cybersecurity", "name": "AI Cybersecurity", "desc": "Threat detection, vulnerability scanning, and secure coding."},
    {"slug": "design-ui", "name": "AI UI/UX & Design", "desc": "Wireframing, landing page builders, and graphic assets."},
    {"slug": "social-media", "name": "AI Social Media Schedulers", "desc": "Post scheduling, engagement analytics, and trend tracking."},
    {"slug": "hr-recruiting", "name": "AI HR & Recruiting", "desc": "Resume screening, candidate matching, and interview bots."},
    {"slug": "healthcare-wellness", "name": "AI Healthcare & Wellness", "desc": "Symptom checkers, fitness planners, and mental health bots."},
    {"slug": "ecommerce-optimizer", "name": "AI E-Commerce Optimizers", "desc": "Product descriptions, pricing optimization, and recommendations."},
    {"slug": "research-academic", "name": "AI Research Assistants", "desc": "Literature reviews, paper summarization, and citation formatting."},
    {"slug": "gaming-npc", "name": "AI Gaming & NPC Generators", "desc": "Procedural content generation, NPC dialogue, and lore creation."},
    {"slug": "avatar-generator", "name": "AI Avatar & Headshot Makers", "desc": "Professional portraits, 3D avatars, and digital twins."},
    {"slug": "music-composer", "name": "AI Music & Beat Composers", "desc": "Instrumental tracks, royalty-free background music, and vocals."},
    {"slug": "prompt-engineering", "name": "AI Prompt Engineering Tools", "desc": "Prompt libraries, optimizers, and testing suites."},
    {"slug": "real-estate", "name": "AI Real Estate Valuators", "desc": "Property valuation, virtual staging, and listing descriptions."},
    {"slug": "travel-planner", "name": "AI Travel Planners", "desc": "Itinerary generators, flight trackers, and tourist guides."},
    {"slug": "architecture-cad", "name": "AI Architecture & CAD", "desc": "Floor plan generators, 3D rendering, and spatial design."},
    {"slug": "podcast-editor", "name": "AI Podcast Editors", "desc": "Noise cancellation, transcript cleaning, and clip extraction."},
    {"slug": "chatbot-builders", "name": "No-Code AI Chatbot Builders", "desc": "Custom knowledge base bots for customer service."},
    {"slug": "logo-branding", "name": "AI Logo & Branding", "desc": "Brand identity kits, vector logos, and color palettes."},
    {"slug": "infographic-maker", "name": "AI Infographic Generators", "desc": "Data charts, mind maps, and workflow diagrams."},
    {"slug": "email-automation", "name": "AI Email Sequence Builders", "desc": "Cold outreach, personalized sequences, and inbox management."},
    {"slug": "lead-generation", "name": "AI Lead Generation", "desc": "Prospect scoring, company enrichment, and contact lookup."},
    {"slug": "survey-analyzer", "name": "AI Survey & Feedback Analyzers", "desc": "Sentiment analysis, open-ended response clustering."},
    {"slug": "meeting-assistant", "name": "AI Meeting Transcribers", "desc": "Zoom/Teams recorders, action item extractors, and notes."},
    {"slug": "resume-builder", "name": "AI Resume & CV Builders", "desc": "ATS-friendly formatting, bullet point enhancer, and cover letters."},
    {"slug": "storytelling", "name": "AI Fiction & Story Writers", "desc": "Novel plotting, character arcs, and scriptwriting."},
    {"slug": "nutrition-diet", "name": "AI Nutrition & Meal Planners", "desc": "Macro tracking, grocery lists, and recipe generators."},
    {"slug": "gardening-plant", "name": "AI Plant & Garden Care", "desc": "Disease diagnosis, watering schedules, and landscaping."},
    {"slug": "astrology-horoscope", "name": "AI Astrology & Tarot", "desc": "Birth chart analysis, astrological forecasts, and readings."},
    {"slug": "event-planner", "name": "AI Event Management", "desc": "Guest list optimization, vendor matching, and invitation copy."},
    {"slug": "pet-care", "name": "AI Pet Care & Training", "desc": "Behavioral tips, breed identification, and vet guides."},
    {"slug": "language-learning", "name": "AI Language Tutors", "desc": "Conversational practice, grammar correction, and vocabulary drills."},
    {"slug": "fashion-stylist", "name": "AI Fashion & Outfit Stylists", "desc": "Virtual try-ons, seasonal capsule wardrobes, and color matching."},
    {"slug": "interior-design", "name": "AI Interior Redecorators", "desc": "Room styling, furniture rearrangement, and paint visualization."},
    {"slug": "genealogy-history", "name": "AI Genealogy Researchers", "desc": "Family tree tracing, historical record indexing, and restoration."},
    {"slug": "spirituality-meditation", "name": "AI Meditation Guides", "desc": "Guided breathing sessions, mindfulness prompts, and sleep stories."},
    {"slug": "automotive-diagnostic", "name": "AI Automotive Diagnostics", "desc": "OBD-II code explainers, repair guides, and maintenance schedules."},
    {"slug": "smart-home", "name": "AI Smart Home Automators", "desc": "Routine optimization, energy saving, and IoT integration."}
]

def generate_html(title, category_name, tool_name, slug, tool_num):
    internal_links = """
    <ul>
        <li><a href="https://indoinves.github.io/">Home Dashboard</a></li>
        <li><a href="https://indoinves.github.io/about.html">About Indoinves</a></li>
        <li><a href="https://indoinves.github.io/contact.html">Contact Support</a></li>
        <li><a href="https://indoinves.github.io/privacy.html">Privacy Policy</a></li>
        <li><a href="https://indoinves.github.io/sitemap.html">Master Sitemap</a></li>
        <li><a href="https://indoinves.github.io/disclaimer.html">Disclaimer</a></li>
        <li><a href="https://indoinves.github.io/terms.html">Terms on Conditional License</a></li>
    </ul>
    """

    external_links = """
    <ul>
        <li><a href="https://openai.com" target="_blank" rel="nofollow">OpenAI Research</a></li>
        <li><a href="https://anthropic.com" target="_blank" rel="nofollow">Anthropic AI</a></li>
        <li><a href="https://deepmind.google" target="_blank" rel="nofollow">Google DeepMind</a></li>
        <li><a href="https://huggingface.co" target="_blank" rel="nofollow">Hugging Face Hub</a></li>
        <li><a href="https://github.com" target="_blank" rel="nofollow">GitHub Open Source</a></li>
        <li><a href="https://arxiv.org" target="_blank" rel="nofollow">arXiv Computer Science Papers</a></li>
        <li><a href="https://pytorch.org" target="_blank" rel="nofollow">PyTorch Framework</a></li>
        <li><a href="https://tensorflow.org" target="_blank" rel="nofollow">TensorFlow Platform</a></li>
        <li><a href="https://www.kaggle.com" target="_blank" rel="nofollow">Kaggle Data Science</a></li>
        <li><a href="https://www.producthunt.com" target="_blank" rel="nofollow">Product Hunt Tech</a></li>
    </ul>
    """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - {tool_name} | Indoinves AI Directory</title>
    <meta name="description" content="Discover comprehensive guides, use cases, and insights for {tool_name} under {category_name}. Powered by Indoinves Global Intelligence.">
    
    <!-- Google AdSense & Verification Meta Tags -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
    <meta name="google-adsense-account" content="ca-pub-8423475960451668">
    <meta name="google-site-verification" content="U1VAgdRlZJWlLXGlGnsAGbZA1TVBp2DG0c6XzQJNonY" />
    
    <!-- Favicon & Manifest -->
    <link rel="icon" type="image/png" href="https://indoinves.github.io/img/indoinves.png">
    <link rel="icon" href="https://indoinves.github.io/indoinves.png" type="image/png" />
    <link rel="manifest" href="https://indoinves.github.io/manifest.json" />

    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; background: #f9f9f9; }}
        header {{ background: #1a1a2e; color: #fff; padding: 20px; text-align: center; }}
        header img {{ width: 60px; height: 60px; vertical-align: middle; margin-right: 15px; }}
        header h1 {{ display: inline-block; font-size: 24px; margin: 0; vertical-align: middle; }}
        nav {{ background: #162447; padding: 10px; text-align: center; }}
        nav a {{ color: #e4e4e4; margin: 0 15px; text-decoration: none; font-weight: bold; }}
        nav a:hover {{ color: #e94560; }}
        .container {{ max-width: 900px; margin: 30px auto; background: #fff; padding: 40px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }}
        .social-share {{ margin: 20px 0; padding: 10px; background: #f1f3f6; border-radius: 5px; text-align: center; }}
        .social-share a {{ margin: 0 10px; text-decoration: none; color: #162447; font-weight: bold; }}
        .toc {{ background: #edf2f7; padding: 20px; border-radius: 6px; margin: 20px 0; }}
        .toc h3 {{ margin-top: 0; }}
        .toc ul {{ padding-left: 20px; }}
        img.featured-img {{ width: 100%; height: auto; border-radius: 6px; margin: 20px 0; }}
        h2 {{ color: #1a1a2e; border-bottom: 2px solid #e4e4e4; padding-bottom: 5px; margin-top: 40px; }}
        footer {{ background: #1a1a2e; color: #fff; text-align: center; padding: 30px 20px; margin-top: 50px; }}
        .footer-links a {{ color: #a0aec0; margin: 0 10px; text-decoration: none; }}
        .footer-links a:hover {{ color: #fff; }}
        .links-section {{ margin: 30px 0; padding: 20px; background: #fffaf0; border-left: 4px solid #ed8936; }}
    </style>
</head>
<body>

    <header>
        <img src="https://indoinves.github.io/indoinves.png" alt="Indoinves Logo">
        <h1>Indoinves AI Directory</h1>
    </header>

    <nav>
        <a href="https://indoinves.github.io/">Home</a>
        <a href="https://indoinves.github.io/{slug}/">Category Index</a>
        <a href="https://indoinves.github.io/contact.html">Contact Us</a>
        <a href="https://indoinves.github.io/sitemap.html">Sitemap</a>
    </nav>

    <div class="container">
        <!-- Unit Iklan Banner AdSense -->
        <div style="margin: 25px 0;">
            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
            <ins class="adsbygoogle"
                 style="display:block"
                 data-ad-client="ca-pub-8423475960451668"
                 data-ad-slot="6147545291"
                 data-ad-format="auto"
                 data-full-width-responsive="true"></ins>
            <script>
                 (adsbygoogle = window.adsbygoogle || []).push({{}});
            </script>
        </div>

        <div class="social-share">
            <span>Share this tool:</span>
            <a href="https://twitter.com/intent/tweet?text=Check%20out%20{tool_name}" target="_blank" rel="nofollow">Twitter</a>
            <a href="https://www.linkedin.com/shareArticle?mini=true&title={tool_name}" target="_blank" rel="nofollow">LinkedIn</a>
            <a href="https://api.whatsapp.com/send?text={tool_name}" target="_blank" rel="nofollow">WhatsApp</a>
        </div>

        <h1>{tool_name}</h1>
        <p><em>Category: {category_name} | Tool ID: #{tool_num}</em></p>

        <img src="https://indoinves.github.io/img/{slug}-{tool_num}.jpg" alt="{tool_name} interface preview and workflow dashboard for {category_name}" class="featured-img">

        <!-- Table of Contents -->
        <div class="toc">
            <h3>Table of Contents</h3>
            <ul>
                <li><a href="#overview">1. Overview and Introduction</a></li>
                <li><a href="#features">2. Key Features and Capabilities</a></li>
                <li><a href="#workflow">3. Step-by-Step Usage Guide</a></li>
                <li><a href="#benefits">4. Benefits for Professionals</a></li>
                <li><a href="#faq">5. Frequently Asked Questions (FAQ)</a></li>
                <li><a href="#resources">6. Internal & External Resources</a></li>
            </ul>
        </div>

        <h2 id="overview">1. Overview and Introduction</h2>
        <p>{tool_name} is an advanced artificial intelligence solution categorized under {category_name}. Designed to optimize modern digital workflows, it empowers creators, developers, and enterprise teams to scale productivity seamlessly. In today's hyper-competitive technological environment, leveraging state-of-the-art AI instruments ensures optimal efficiency and precise output generation.</p>

        <h2 id="features">2. Key Features and Capabilities</h2>
        <ul>
            <li><strong>Automated Processing:</strong> Instantly execute heavy computations and asset generation with minimal human intervention.</li>
            <li><strong>High Precision:</strong> Fine-tuned neural network architectures ensure industry-grade accuracy and reliability.</li>
            <li><strong>API Integration:</strong> Easily connect with existing cloud infrastructure, databases, and third-party SaaS tools.</li>
            <li><strong>Scalable Architecture:</strong> Handle large workloads, batch processing, and multi-user environments effortlessly.</li>
        </ul>

        <h2 id="workflow">3. Step-by-Step Usage Guide</h2>
        <ol>
            <li><strong>Account Setup & Authentication:</strong> Navigate to the official platform, register your secure credentials, and configure your workspace profile.</li>
            <li><strong>Input Configuration:</strong> Provide your prompt, dataset, or media assets according to your project requirements.</li>
            <li><strong>Parameter Tuning:</strong> Adjust advanced settings such as temperature, output length, or rendering quality.</li>
            <li><strong>Execution & Export:</strong> Run the generation sequence and download your polished results in your preferred format.</li>
        </ol>

        <!-- Unit Iklan Autorelaxed AdSense -->
        <div style="margin: 25px 0;">
            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
            <ins class="adsbygoogle"
                 style="display:block"
                 data-ad-format="autorelaxed"
                 data-ad-client="ca-pub-8423475960451668"
                 data-ad-slot="7183276396"></ins>
            <script>
                 (adsbygoogle = window.adsbygoogle || []).push({{}});
            </script>
        </div>

        <h2 id="benefits">4. Benefits for Professionals</h2>
        <p>By integrating {tool_name} into your daily operations, your team can reduce turnaround time by up to 70%. The system eliminates repetitive manual bottlenecks, allowing professionals to focus on creative strategy, high-level decision making, and core product development.</p>

        <h2 id="faq">5. Frequently Asked Questions (FAQ)</h2>
        <h3>What is {tool_name}?</h3>
        <p>{tool_name} is a cutting-edge software utility engineered to streamline tasks within the {category_name} ecosystem.</p>

        <h3>Is prior coding experience required?</h3>
        <p>No, the platform features an intuitive, user-friendly interface suitable for both beginners and seasoned technical experts.</p>

        <h3>Can I export results for commercial use?</h3>
        <p>Yes, all generated outputs comply with standard commercial licensing agreements when using authorized plans.</p>

        <h2 id="resources">6. Internal & External Resources</h2>
        <div class="links-section">
            <h3>Internal Directory Links</h3>
            {internal_links}
        </div>

        <div class="links-section">
            <h3>External Authoritative References</h3>
            {external_links}
        </div>
    </div>

    <!-- Footer -->
    <footer>
        <div class="footer-links">
            <a href="https://indoinves.github.io/">Home</a>
            <a href="https://indoinves.github.io/about.html">About Us</a>
            <a href="https://indoinves.github.io/contact.html">Contact Us</a>
            <a href="https://indoinves.github.io/privacy.html">Privacy Policy</a>
            <a href="https://indoinves.github.io/sitemap.html">Sitemap</a>
            <a href="https://indoinves.github.io/disclaimer.html">Disclaimer</a>
            <a href="https://indoinves.github.io/terms.html">Terms on Conditional License</a>
        </div>
        <p>&copy; 2026 Indoinves. All Rights Reserved. Global Intelligence Report & Explorer Tools.</p>
    </footer>

</body>
</html>
"""
    return html

def generate_category_index(cat):
    slug = cat["slug"]
    name = cat["name"]
    
    tools_list_html = ""
    for i in range(1, 31):
        tool_name = f"{name} Tool {i}"
        tools_list_html += f'<li><a href="tool-{i}.html">{tool_name}</a></li>\\n'
        
    internal_links = """
    <ul>
        <li><a href="https://indoinves.github.io/">Home Dashboard</a></li>
        <li><a href="https://indoinves.github.io/about.html">About Indoinves</a></li>
        <li><a href="https://indoinves.github.io/contact.html">Contact Support</a></li>
        <li><a href="https://indoinves.github.io/privacy.html">Privacy Policy</a></li>
        <li><a href="https://indoinves.github.io/sitemap.html">Master Sitemap</a></li>
        <li><a href="https://indoinves.github.io/disclaimer.html">Disclaimer</a></li>
        <li><a href="https://indoinves.github.io/terms.html">Terms on Conditional License</a></li>
    </ul>
    """
    
    external_links = """
    <ul>
        <li><a href="https://openai.com" target="_blank" rel="nofollow">OpenAI Research</a></li>
        <li><a href="https://anthropic.com" target="_blank" rel="nofollow">Anthropic AI</a></li>
        <li><a href="https://deepmind.google" target="_blank" rel="nofollow">Google DeepMind</a></li>
        <li><a href="https://huggingface.co" target="_blank" rel="nofollow">Hugging Face Hub</a></li>
        <li><a href="https://github.com" target="_blank" rel="nofollow">GitHub Open Source</a></li>
        <li><a href="https://arxiv.org" target="_blank" rel="nofollow">arXiv Computer Science Papers</a></li>
        <li><a href="https://pytorch.org" target="_blank" rel="nofollow">PyTorch Framework</a></li>
        <li><a href="https://tensorflow.org" target="_blank" rel="nofollow">TensorFlow Platform</a></li>
        <li><a href="https://www.kaggle.com" target="_blank" rel="nofollow">Kaggle Data Science</a></li>
        <li><a href="https://www.producthunt.com" target="_blank" rel="nofollow">Product Hunt Tech</a></li>
    </ul>
    """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - 30 AI Tools Directory | Indoinves</title>
    <meta name="description" content="Explore 30 specialized {name} tools and utilities with comprehensive guides, reviews, and workflows.">
    
    <!-- Google AdSense & Verification Meta Tags -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
    <meta name="google-adsense-account" content="ca-pub-8423475960451668">
    <meta name="google-site-verification" content="U1VAgdRlZJWlLXGlGnsAGbZA1TVBp2DG0c6XzQJNonY" />
    
    <link rel="icon" type="image/png" href="https://indoinves.github.io/img/indoinves.png">
    <link rel="icon" href="https://indoinves.github.io/indoinves.png" type="image/png" />
    <link rel="manifest" href="https://indoinves.github.io/manifest.json" />

    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; background: #f9f9f9; }}
        header {{ background: #1a1a2e; color: #fff; padding: 20px; text-align: center; }}
        header img {{ width: 60px; height: 60px; vertical-align: middle; margin-right: 15px; }}
        header h1 {{ display: inline-block; font-size: 24px; margin: 0; vertical-align: middle; }}
        nav {{ background: #162447; padding: 10px; text-align: center; }}
        nav a {{ color: #e4e4e4; margin: 0 15px; text-decoration: none; font-weight: bold; }}
        nav a:hover {{ color: #e94560; }}
        .container {{ max-width: 900px; margin: 30px auto; background: #fff; padding: 40px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }}
        .social-share {{ margin: 20px 0; padding: 10px; background: #f1f3f6; border-radius: 5px; text-align: center; }}
        .social-share a {{ margin: 0 10px; text-decoration: none; color: #162447; font-weight: bold; }}
        h2 {{ color: #1a1a2e; border-bottom: 2px solid #e4e4e4; padding-bottom: 5px; margin-top: 40px; }}
        ul.tools-grid {{ list-style-type: none; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }}
        ul.tools-grid li {{ background: #f8fafc; padding: 15px; border: 1px solid #e2e8f0; border-radius: 6px; }}
        ul.tools-grid li a {{ text-decoration: none; color: #2b6cb0; font-weight: bold; }}
        ul.tools-grid li a:hover {{ text-decoration: underline; }}
        footer {{ background: #1a1a2e; color: #fff; text-align: center; padding: 30px 20px; margin-top: 50px; }}
        .footer-links a {{ color: #a0aec0; margin: 0 10px; text-decoration: none; }}
        .footer-links a:hover {{ color: #fff; }}
        .links-section {{ margin: 30px 0; padding: 20px; background: #fffaf0; border-left: 4px solid #ed8936; }}
    </style>
</head>
<body>

    <header>
        <img src="https://indoinves.github.io/indoinves.png" alt="Indoinves Logo">
        <h1>Indoinves AI Directory</h1>
    </header>

    <nav>
        <a href="https://indoinves.github.io/">Home</a>
        <a href="https://indoinves.github.io/contact.html">Contact Us</a>
        <a href="https://indoinves.github.io/sitemap.html">Sitemap</a>
    </nav>

    <div class="container">
        <!-- Unit Iklan Banner AdSense -->
        <div style="margin: 25px 0;">
            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
            <ins class="adsbygoogle"
                 style="display:block"
                 data-ad-client="ca-pub-8423475960451668"
                 data-ad-slot="6147545291"
                 data-ad-format="auto"
                 data-full-width-responsive="true"></ins>
            <script>
                 (adsbygoogle = window.adsbygoogle || []).push({{}});
            </script>
        </div>

        <div class="social-share">
            <span>Share category:</span>
            <a href="https://twitter.com/intent/tweet?text=Check%20out%20{name}" target="_blank" rel="nofollow">Twitter</a>
            <a href="https://www.linkedin.com/shareArticle?mini=true&title={name}" target="_blank" rel="nofollow">LinkedIn</a>
            <a href="https://api.whatsapp.com/send?text={name}" target="_blank" rel="nofollow">WhatsApp</a>
        </div>

        <h1>{name}</h1>
        <p>{cat["desc"]}</p>

        <img src="https://indoinves.github.io/img/{slug}-banner.jpg" alt="Comprehensive overview of {name} artificial intelligence tools and workflow solutions" style="width:100%; border-radius:6px; margin:20px 0;">

        <h2>List of 30 {name} Utilities</h2>
        <ul class="tools-grid">
            {tools_list_html}
        </ul>

        <!-- Unit Iklan Autorelaxed AdSense -->
        <div style="margin: 25px 0;">
            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
            <ins class="adsbygoogle"
                 style="display:block"
                 data-ad-format="autorelaxed"
                 data-ad-client="ca-pub-8423475960451668"
                 data-ad-slot="7183276396"></ins>
            <script>
                 (adsbygoogle = window.adsbygoogle || []).push({{}});
            </script>
        </div>

        <div class="links-section">
            <h3>Internal Directory Links</h3>
            {internal_links}
        </div>

        <div class="links-section">
            <h3>External Authoritative References</h3>
            {external_links}
        </div>
    </div>

    <footer>
        <div class="footer-links">
            <a href="https://indoinves.github.io/">Home</a>
            <a href="https://indoinves.github.io/about.html">About Us</a>
            <a href="https://indoinves.github.io/contact.html">Contact Us</a>
            <a href="https://indoinves.github.io/privacy.html">Privacy Policy</a>
            <a href="https://indoinves.github.io/sitemap.html">Sitemap</a>
            <a href="https://indoinves.github.io/disclaimer.html">Disclaimer</a>
            <a href="https://indoinves.github.io/terms.html">Terms on Conditional License</a>
        </div>
        <p>&copy; 2026 Indoinves. All Rights Reserved. Global Intelligence Report & Explorer Tools.</p>
    </footer>

</body>
</html>
"""
    return html

def main():
    print(f"Starting generation of 50 categories with 30 tools each...")
    for cat in AI_CATEGORIES:
        slug = cat["slug"]
        cat_name = cat["name"]
        os.makedirs(slug, exist_ok=True)
        
        # Generate category index.html
        cat_index_content = generate_category_index(cat)
        with open(os.path.join(slug, "index.html"), "w", encoding="utf-8") as f:
            f.write(cat_index_content)
            
        # Generate 30 tool pages per category
        for i in range(1, 31):
            tool_name = f"{cat_name} Tool {i}"
            tool_filename = f"tool-{i}.html"
            tool_content = generate_html(tool_name, cat_name, tool_name, slug, i)
            with open(os.path.join(slug, tool_filename), "w", encoding="utf-8") as f:
                f.write(tool_content)
        print(f"Generated category: {slug} (30 tools created)")

    print("All 50 categories and 1,500 tool pages generated successfully!")

if __name__ == "__main__":
    main()
