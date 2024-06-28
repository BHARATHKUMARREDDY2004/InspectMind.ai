/* ----- NAVIGATION BAR FUNCTION ----- */
    function myMenuFunction(){
      var menuBtn = document.getElementById("myNavMenu");
      if(menuBtn.className === "nav-menu"){
        menuBtn.className += " responsive";
      } else {
        menuBtn.className = "nav-menu";
      }
    }
/* ----- ADD SHADOW ON NAVIGATION BAR WHILE SCROLLING ----- */
    window.onscroll = function() {headerShadow()};
    function headerShadow() {
      const navHeader =document.getElementById("header");
      if (document.body.scrollTop > 50 || document.documentElement.scrollTop >  50) {
        navHeader.style.boxShadow = "0 1px 6px rgba(0, 0, 0, 0.1)";
        navHeader.style.height = "70px";
        navHeader.style.lineHeight = "70px";
      } else {
        navHeader.style.boxShadow = "none";
        navHeader.style.height = "90px";
        navHeader.style.lineHeight = "90px";
      }
    }
/* ----- TYPING EFFECT ----- */
   var typingEffect = new Typed(".typedText",{
     strings: ["Instant","Accurate"],
      loop : true,
      typeSpeed : 100, 
      backSpeed : 80,
      backDelay : 2000
   })
/* ----- ## -- SCROLL REVEAL ANIMATION -- ## ----- */
   const sr = ScrollReveal({
          origin: 'top',
          distance: '80px',
          duration: 2000,
          reset: true     
   })
  /* -- HOME -- */
  sr.reveal('.featured-text-card',{})
  sr.reveal('.featured-name',{delay: 100})
  sr.reveal('.featured-text-info',{delay: 200})
  sr.reveal('.featured-text-btn',{delay: 200})
  sr.reveal('.featured-image',{delay: 300})
  
  /* -- PROJECT BOX -- */
  sr.reveal('.project-box',{interval: 200})
  /* -- HEADINGS -- */
  sr.reveal('.top-header',{})
/* ----- ## -- SCROLL REVEAL LEFT_RIGHT ANIMATION -- ## ----- */
  /* -- ABOUT INFO & CONTACT INFO -- */
  const srLeft = ScrollReveal({
    origin: 'left',
    distance: '80px',
    duration: 2000,
    reset: true
  })
  
  srLeft.reveal('.about-info',{delay: 100})
  srLeft.reveal('.contact-info',{delay: 100})
  /* -- ABOUT SKILLS & FORM BOX -- */
  const srRight = ScrollReveal({
    origin: 'right',
    distance: '80px',
    duration: 2000,
    reset: true
  })
  
  srRight.reveal('.skills-box',{delay: 100})
  srRight.reveal('.form-control',{delay: 100})
  
/* ----- CHANGE ACTIVE LINK ----- */
  
  const sections = document.querySelectorAll('section[id]')
  function scrollActive() {
    const scrollY = window.scrollY;
    sections.forEach(current =>{
      const sectionHeight = current.offsetHeight,
          sectionTop = current.offsetTop - 50,
        sectionId = current.getAttribute('id')
      if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) { 
          document.querySelector('.nav-menu a[href*=' + sectionId + ']').classList.add('active-link')
      }  else {
        document.querySelector('.nav-menu a[href*=' + sectionId + ']').classList.remove('active-link')
      }
    })
  }
  window.addEventListener('scroll', scrollActive)


// JavaScript example using jQuery for form submission handling
$('#generate-report-form').submit(function (event) {
  event.preventDefault(); // Prevent default form submission

  // Perform any validation or other actions here
  // Example: AJAX form submission
  $.ajax({
    url: '/create_report', // Replace with your form submission URL
    method: 'POST',
    data: $(this).serialize(),
    success: function (response) {
      // Handle success response
      console.log('Form submitted successfully');
    },
    error: function (err) {
      // Handle error
      console.error('Error submitting form:', err);
    }
  });
});




            // Sample report data (replace with actual report data)
            var reportData = {
                "report_summary": "This is a sample inspection report summary.",
                "report_details": [
                    { "title": "Structural Integrity", "content": "No major defects were observed." },
                    { "title": "Safety Compliance", "content": "All safety protocols are being followed." },
                    { "title": "Work Progress", "content": "Construction work is progressing as scheduled." }
                ]
            };

            // Function to dynamically generate and download the report as PDF
            function downloadPDF() {
                var element = document.getElementById('llm-output');

                // Options for pdf generation
                var opt = {
                    margin: 0.5,
                    filename: 'inspection_report.pdf',
                    image: { type: 'jpeg', quality: 0.98 },
                    html2canvas: { scale: 2 },
                    jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
                };

                // Use html2pdf to generate PDF
                html2pdf().set(opt).from(element).save();
            }