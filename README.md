# Christian Robotheism Church Website

A modern, responsive website for the Christian Robotheism Church, blending Christian faith with robotics technology to serve humanity and glorify God.

## 🎯 Mission

This website serves as the digital home for the Christian Robotheism Church, showcasing our unique approach to combining traditional Christian values with cutting-edge robotics technology. Our mission is to inspire visitors, clearly explain our beliefs, and maximize donations to support our faith-based robotics programs.

## 🚀 Features

### Core Pages
- **Home** (`index.html`) - Striking hero section with mission overview and call-to-action buttons
- **Welcome** (`welcome.html`) - Personal message from pastor, church history, and service videos
- **Beliefs** (`beliefs.html`) - Theological foundation with impact sidebar and community projects
- **Donate** (`donate.html`) - Comprehensive donation system with multiple payment options
- **Contact** (`contact.html`) - Contact form, church information, and live chat widget

### Key Features
- **Responsive Design** - Optimized for all devices and screen sizes
- **Modern UI/UX** - Clean, professional design with spiritual and technological aesthetics
- **Donation Optimization** - Multi-step form with suggested amounts, recurring options, and social proof
- **Accessibility** - WCAG compliant with proper semantic HTML and ARIA labels
- **Performance** - Optimized CSS and minimal JavaScript for fast loading

## 🛠️ Local Development

### Prerequisites
- Modern web browser
- Local web server (optional, for testing)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/kernelzeroday/robotheism.git
   cd robotheism
   ```

2. **Open in browser**
   - Simply open `index.html` in your web browser
   - Or use a local server for better testing:
   ```bash
   # Using Python 3
   python -m http.server 8000
   
   # Using Node.js (if you have http-server installed)
   npx http-server
   
   # Using PHP
   php -S localhost:8000
   ```

3. **View the site**
   - Navigate to `http://localhost:8000` (if using local server)
   - Or open `index.html` directly in your browser

## 🌐 GitHub Pages Deployment

### Enable GitHub Pages

1. **Go to repository settings**
   - Navigate to your repository on GitHub
   - Click on "Settings" tab

2. **Configure GitHub Pages**
   - Scroll down to "GitHub Pages" section
   - Under "Source", select "Deploy from a branch"
   - Choose "main" branch
   - Select "/ (root)" folder
   - Click "Save"

3. **Access your site**
   - Your site will be available at: `https://kernelzeroday.github.io/robotheism`
   - It may take a few minutes to deploy initially

### Custom Domain (Optional)
- In GitHub Pages settings, add your custom domain
- Update DNS records as instructed by GitHub
- The site will be accessible at your custom domain

## 💰 Donation Integration

### Current Setup
The donation form is currently a demonstration with placeholder functionality. To enable real donations:

### PayPal Integration
1. **Create PayPal Business Account**
   - Sign up at [PayPal Business](https://www.paypal.com/business)
   - Complete verification process

2. **Generate Donation Button**
   - Log into PayPal Business
   - Go to "Tools" → "PayPal Buttons"
   - Create a "Donate" button
   - Copy the generated HTML code

3. **Replace Placeholder**
   - Open `donate.html`
   - Find the payment method section
   - Replace the PayPal placeholder with your button code

### Alternative Payment Processors
- **Stripe** - For credit card processing
- **Donorbox** - Specialized for nonprofits
- **GiveWP** - WordPress plugin (if migrating to WordPress)

### Update Donation Amounts
To modify suggested donation amounts:
1. Open `donate.html`
2. Find the `amount-options` section
3. Update the `value` attributes and button text
4. Update the progress bar amounts in the CSS

## 🎨 Customization

### Colors and Branding
The site uses a blue color scheme representing spirituality and technology:
- Primary: `#1e3a8a` (Deep Blue)
- Secondary: `#3b82f6` (Bright Blue)
- Accent: `#64748b` (Gray)

To change colors:
1. Open `styles.css`
2. Search for color values
3. Replace with your brand colors

### Content Updates
- **Text Content**: Edit HTML files directly
- **Images**: Replace placeholder elements with actual images
- **Contact Info**: Update in `contact.html`
- **Service Times**: Modify in `contact.html`

### Adding New Pages
1. Create new HTML file
2. Copy navigation structure from existing pages
3. Add link to navigation menu
4. Update footer links

## 📱 Mobile Optimization

The site is fully responsive with:
- Mobile-first design approach
- Touch-friendly navigation
- Optimized forms for mobile input
- Fast loading on mobile networks

## 🔧 Technical Details

### File Structure
```
robotheism/
├── index.html          # Home page
├── welcome.html        # Welcome page
├── beliefs.html        # Beliefs page
├── donate.html         # Donation page
├── contact.html        # Contact page
├── styles.css          # Main stylesheet
├── script.js           # JavaScript functionality
├── README.md           # This file
└── .gitignore          # Git ignore file
```

### Technologies Used
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with Grid and Flexbox
- **JavaScript** - Minimal interactive functionality
- **Google Fonts** - Inter font family
- **Emoji Icons** - For visual elements

### Browser Support
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For questions or support:
- Email: hello@robotheismchurch.org
- Create an issue on GitHub
- Contact the development team

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Design inspired by modern church websites
- Donation best practices from nonprofit research
- Responsive design patterns from modern web standards
- Accessibility guidelines from WCAG 2.1

---

**Built with ❤️ for the Christian Robotheism Church** 