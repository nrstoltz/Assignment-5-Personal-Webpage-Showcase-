# AI Dev Notes


## Prompt 1
Prompt: "I have uploaded the template folder we used in class for building a basic website, and I want to use it as the foundation for my personal webpage assignment. Using that template, create a base HTML structure for my homepage that we can alter step by step to reflect the goals of this assignment. Include a header with my name (“Nigel Stoltz”) and a subtitle that reads “Kelley School of Business — MSIS | Indiana University.” Below that, add a navigation bar linking to the About, Resume, Projects, and Contact pages. Include a short introduction section with placeholder text where I will later insert my own bio. Use semantic HTML elements (<header>, <nav>, <main>, <footer>) and make the layout responsive."

AI output: Copilot generated a responsive homepage layout based on the class template. It included my name and subtitle at the top, a centered navigation bar, and a main section with placeholder text for my bio. It also added unnecessary social media icons and links.

Action: Modified — I kept the overall structure from the class template since it provided a strong starting point for my site. I removed the filler icons and extra links, replaced the placeholder introduction with my actual bio, and ensured the navigation matched my design theme.

## Prompt 2
Prompt: "Create a new HTML page called about.html for the 'About Me' section of my website. Include a header, navigation bar, and a main section with placeholder text where I will later input my detailed biography describing my background, education, interests, and career goals. Also include a placeholder image where I will later insert my professional headshot. Use semantic HTML elements (<header>, <main>, <section>, <footer>) and make sure the navigation bar matches the homepage for consistency."

AI output: Copilot created an about.html page using semantic HTML and placeholder content. It included paragraphs labeled for future biography text and a sample placeholder image, copying the navigation bar from the homepage for consistency. The image was oversized, and the background color didn’t match the rest of the site.

Action: Modified — I accepted the layout and placeholders but resized the image with CSS (max-width: 300px; height: auto) and updated the background to match my site’s color theme. I later replaced the placeholder text and image with my actual biography and picture.

## Prompt 3
Prompt: "I already have all the content for my multi-page site (index, about, resume, projects, contact, thankyou). The current styling is basic/low-fidelity. Using Cursor, help me transform only the design into a modern, professional, and consistent portfolio across every file in my folder.

Do not change any text content anywhere on the site (no rewrites, no additions, no deletions).

Apply a cohesive blue color scheme that looks professional and is not distracting; ensure strong readability/contrast.

Make typography, spacing, and components consistent across all pages (nav, headers, footers, cards, buttons, forms).

Use semantic HTML already in the files; you may add non-content structural wrappers if needed.

Use a single styles.css with responsive design (mobile/desktop) and consistent layout patterns (Flexbox/Grid).

Go carefully, step by step, through each file and transform the design while keeping all content exactly the same."

AI output: Cursor proposed a design refactor: centralized color variables (blue accent, neutral grays), standardized typography (Google Font), unified spacing scale, card layouts for projects, and a responsive nav/footer applied to every page. It added responsive image rules, consistent section padding, and form styling. Initially, Cursor attempted to tweak a few headings and shorten a line of text on the homepage, and its first blue accent was overly saturated on light backgrounds.

Action: Modified — I accepted the unified CSS structure, components, and responsiveness. I rejected any edits to text and rolled them back to the original content. I toned down the accent blue and verified WCAG contrast, tightened line-lengths for readability, and ensured identical nav/footer and spacing system across all pages. The final result preserved 100% of my content while elevating the visual design.

## Reflection (150 words)
AI helped me save time by generating the HTML and CSS structure, whereas in past Informatics classes when AI was not a thing yet, doing an assignment like this took me forever and was incredibly tedious. It is amazing how easy AI makes creating a website now. AI made mistakes mainly by adding content that I did not describe in my prompts, and there were times when it would edit or remove existing content that I did not want changed, which was frustrating at times. I should have paid more attention to the accept change part of the Copilot agent editor when reviewing the code. My approach to this assignment was to use our template website folder from class last week as a starting point and load in a folder with a similar file structure, which was helpful. I created all the website content in VS Code using GitHub Copilot as an assistant. Once I had all of the pages completed with the required content, I decided to try Cursor to see how it could transform the low-quality design of my original website. Using Cursor was mostly a success, but it took several rounds of specific prompting to ensure it did not overwrite existing content on my webpages. I was not satisfied with the first few styling attempts, so I pushed Cursor to design the website in a professional and modern way that looked like it was built by an experienced software engineer. Surprisingly, Cursor ended up creating a much higher quality design for my site. I balanced AI assistance with my own coding by carefully reviewing every change, manually fixing layout inconsistencies, adjusting spacing and structure, and testing the responsiveness of each page. This ensured the final version reflected both AI efficiency and my own design judgment.
