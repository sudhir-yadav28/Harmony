import re

html_file = "tms.html"

with open(html_file, "r") as f:
    content = f.read()

# The target block starts with <!-- FAQ Section --> and ends just before <!-- CTA Section -->
start_tag = "<!-- FAQ Section -->"
end_tag = "<!-- CTA Section -->"

new_faq_html = """<!-- FAQ Section -->
    <section class="py-5 bg-light-beige">
        <div class="container py-5">
            <h2 class="serif-font display-4 mb-5 text-center text-dark" style="margin-bottom: 3.5rem !important;">Frequently Asked Deep TMS Therapy Questions</h2>

            <!-- Box Wrapper Matching Screenshot -->
            <div class="rounded-top-5 p-4 p-md-5" style="border: 1px solid rgba(194, 92, 42, 0.3); border-bottom: none; background-color: #F0EFEA;">
                <div class="row g-5">
                    
                    <!-- Column 1 -->
                    <div class="col-lg-6">
                        
                        <!-- Category 1 -->
                        <p class="text-uppercase x-small fw-bold mb-3 ls-1" style="color: #c25e28;">ELIGIBILITY AND SAFETY</p>
                        <div class="accordion mb-5" id="accordionTMSLeft1">
                            <!-- Q1 -->
                            <div class="mb-3">
                                <button class="btn w-100 text-start py-3 px-4 rounded-pill shadow-sm d-flex justify-content-between align-items-center fw-bold text-dark small border-0" type="button" data-bs-toggle="collapse" data-bs-target="#faq1" style="background-color: #E1E0D7;">
                                    Is TMS Right for You? 
                                    <span class="bg-white rounded-circle flex-shrink-0 d-flex align-items-center justify-content-center shadow-sm" style="width: 24px; height: 24px;">
                                        <svg width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M1 1L5 5L9 1" stroke="#6c757d" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                        </svg>
                                    </span>
                                </button>
                                <div class="collapse mt-2 px-3" id="faq1">
                                    <div class="card card-body border-0 bg-transparent text-muted small fw-light">TMS is ideal for adults and adolescents (15+) struggling with depression, anxiety, or OCD who haven't found sufficient relief from medication.</div>
                                </div>
                            </div>
                            <!-- Q2 -->
                            <div class="mb-3">
                                <button class="btn w-100 text-start py-3 px-4 rounded-pill shadow-sm d-flex justify-content-between align-items-center fw-bold text-dark small border-0" type="button" data-bs-toggle="collapse" data-bs-target="#faq2" style="background-color: #E1E0D7;">
                                    Is TMS Safe? 
                                    <span class="bg-white rounded-circle flex-shrink-0 d-flex align-items-center justify-content-center shadow-sm" style="width: 24px; height: 24px;">
                                        <svg width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M1 1L5 5L9 1" stroke="#6c757d" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                        </svg>
                                    </span>
                                </button>
                                <div class="collapse mt-2 px-3" id="faq2">
                                    <div class="card card-body border-0 bg-transparent text-muted small fw-light">Yes, it is FDA-cleared and considered very safe with minimal side effects.</div>
                                </div>
                            </div>
                            <!-- Q3 -->
                            <div class="mb-3">
                                <button class="btn w-100 text-start py-3 px-4 rounded-pill shadow-sm d-flex justify-content-between align-items-center fw-bold text-dark small border-0" type="button" data-bs-toggle="collapse" data-bs-target="#faq3" style="background-color: #E1E0D7;">
                                    What Risks or Side Effects Should I Expect? 
                                    <span class="bg-white rounded-circle flex-shrink-0 d-flex align-items-center justify-content-center shadow-sm" style="width: 24px; height: 24px;">
                                        <svg width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M1 1L5 5L9 1" stroke="#6c757d" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                        </svg>
                                    </span>
                                </button>
                                <div class="collapse mt-2 px-3" id="faq3">
                                    <div class="card card-body border-0 bg-transparent text-muted small fw-light">Most common side effects are mild scalp discomfort or headache, which typically go away after the first few sessions.</div>
                                </div>
                            </div>
                        </div>

                        <!-- Category 2 -->
                        <p class="text-uppercase x-small fw-bold mb-3 ls-1" style="color: #c25e28;">EFFECTIVENESS AND RESULTS</p>
                        <div class="accordion" id="accordionTMSLeft2">
                            <!-- Q4 -->
                            <div class="mb-3">
                                <button class="btn w-100 text-start py-3 px-4 rounded-pill shadow-sm d-flex justify-content-between align-items-center fw-bold text-dark small border-0" type="button" data-bs-toggle="collapse" data-bs-target="#faq4" style="background-color: #E1E0D7;">
                                    How Effective Is TMS? 
                                    <span class="bg-white rounded-circle flex-shrink-0 d-flex align-items-center justify-content-center shadow-sm" style="width: 24px; height: 24px;">
                                        <svg width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M1 1L5 5L9 1" stroke="#6c757d" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                        </svg>
                                    </span>
                                </button>
                                <div class="collapse mt-2 px-3" id="faq4">
                                    <div class="card card-body border-0 bg-transparent text-muted small fw-light">It is highly effective, with response rates around 70-80% and remission rates near 50% for treatment-resistant patients.</div>
                                </div>
                            </div>
                            <!-- Q5 -->
                            <div class="mb-3">
                                <button class="btn w-100 text-start py-3 px-4 rounded-pill shadow-sm d-flex justify-content-between align-items-center fw-bold text-dark small border-0" type="button" data-bs-toggle="collapse" data-bs-target="#faq5" style="background-color: #E1E0D7;">
                                    How Soon Will I See Results? 
                                    <span class="bg-white rounded-circle flex-shrink-0 d-flex align-items-center justify-content-center shadow-sm" style="width: 24px; height: 24px;">
                                        <svg width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M1 1L5 5L9 1" stroke="#6c757d" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                        </svg>
                                    </span>
                                </button>
                                <div class="collapse mt-2 px-3" id="faq5">
                                    <div class="card card-body border-0 bg-transparent text-muted small fw-light">Most patients notice improvements within 2-3 weeks of daily treatment.</div>
                                </div>
                            </div>
                            <!-- Q6 -->
                            <div class="mb-3">
                                <button class="btn w-100 text-start py-3 px-4 rounded-pill shadow-sm d-flex justify-content-between align-items-center fw-bold text-dark small border-0" type="button" data-bs-toggle="collapse" data-bs-target="#faq6" style="background-color: #E1E0D7;">
                                    How Long Do the Benefits Last? 
                                    <span class="bg-white rounded-circle flex-shrink-0 d-flex align-items-center justify-content-center shadow-sm" style="width: 24px; height: 24px;">
                                        <svg width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M1 1L5 5L9 1" stroke="#6c757d" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                        </svg>
                                    </span>
                                </button>
                                <div class="collapse mt-2 px-3" id="faq6">
                                    <div class="card card-body border-0 bg-transparent text-muted small fw-light">Benefits are durable and can last for a year or more. Some maintenance may be needed.</div>
                                </div>
                            </div>
                            <!-- Q7 -->
                            <div class="mb-3">
                                <button class="btn w-100 text-start py-3 px-4 rounded-pill shadow-sm d-flex justify-content-between align-items-center fw-bold text-dark small border-0" type="button" data-bs-toggle="collapse" data-bs-target="#faq7" style="background-color: #E1E0D7;">
                                    Why is Deep TMS considered more effective? 
                                    <span class="bg-white rounded-circle flex-shrink-0 d-flex align-items-center justify-content-center shadow-sm" style="width: 24px; height: 24px;">
                                        <svg width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M1 1L5 5L9 1" stroke="#6c757d" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                        </svg>
                                    </span>
                                </button>
                                <div class="collapse mt-2 px-3" id="faq7">
                                    <div class="card card-body border-0 bg-transparent text-muted small fw-light">The H-Coil technology reaches deeper and broader brain structures than traditional coils.</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Column 2 -->
                    <div class="col-lg-6">
                        
                        <!-- Category 3 -->
                        <p class="text-uppercase x-small fw-bold mb-3 ls-1" style="color: #c25e28;">THE TREATMENT EXPERIENCE</p>
                        <div class="accordion mb-5" id="accordionTMSRight1">
                            <!-- Q8 -->
                            <div class="mb-3">
                                <button class="btn w-100 text-start py-3 px-4 rounded-pill shadow-sm d-flex justify-content-between align-items-center fw-bold text-dark small border-0" type="button" data-bs-toggle="collapse" data-bs-target="#faq8" style="background-color: #E1E0D7;">
                                    What Does TMS Feel Like? 
                                    <span class="bg-white rounded-circle flex-shrink-0 d-flex align-items-center justify-content-center shadow-sm" style="width: 24px; height: 24px;">
                                        <svg width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M1 1L5 5L9 1" stroke="#6c757d" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                        </svg>
                                    </span>
                                </button>
                                <div class="collapse mt-2 px-3" id="faq8">
                                    <div class="card card-body border-0 bg-transparent text-muted small fw-light">You'll feel a tapping sensation on the head. It is generally well-tolerated.</div>
                                </div>
                            </div>
                            <!-- Q9 -->
                            <div class="mb-3">
                                <button class="btn w-100 text-start py-3 px-4 rounded-pill shadow-sm d-flex justify-content-between align-items-center fw-bold text-dark small border-0" type="button" data-bs-toggle="collapse" data-bs-target="#faq9" style="background-color: #E1E0D7;">
                                    Is Deep TMS comfortable? 
                                    <span class="bg-white rounded-circle d-flex align-items-center justify-content-center shadow-sm" style="width: 24px; height: 24px;">
                                        <i class="fa-solid fa-chevron-down text-muted" style="font-size: 0.7rem; font-weight: 900;"></i>
                                    </span>
                                </button>
                                <div class="collapse mt-2 px-3" id="faq9">
                                    <div class="card card-body border-0 bg-transparent text-muted small fw-light">Yes, the H-Coil helmet is cushioned and designed for patient comfort.</div>
                                </div>
                            </div>
                            <!-- Q10 -->
                            <div class="mb-3">
                                <button class="btn w-100 text-start py-3 px-4 rounded-pill shadow-sm d-flex justify-content-between align-items-center fw-bold text-dark small border-0" type="button" data-bs-toggle="collapse" data-bs-target="#faq10" style="background-color: #E1E0D7;">
                                    How Long Does Treatment Take? 
                                    <span class="bg-white rounded-circle d-flex align-items-center justify-content-center shadow-sm" style="width: 24px; height: 24px;">
                                        <i class="fa-solid fa-chevron-down text-muted" style="font-size: 0.7rem; font-weight: 900;"></i>
                                    </span>
                                </button>
                                <div class="collapse mt-2 px-3" id="faq10">
                                    <div class="card card-body border-0 bg-transparent text-muted small fw-light">Each session is about 20 minutes. A full course is typically 4-6 weeks.</div>
                                </div>
                            </div>
                            <!-- Q11 -->
                            <div class="mb-3">
                                <button class="btn w-100 text-start py-3 px-4 rounded-pill shadow-sm d-flex justify-content-between align-items-center fw-bold text-dark small border-0" type="button" data-bs-toggle="collapse" data-bs-target="#faq11" style="background-color: #E1E0D7;">
                                    Can I Continue My Current Medication While Doing TMS? 
                                    <span class="bg-white rounded-circle d-flex align-items-center justify-content-center shadow-sm" style="width: 24px; height: 24px;">
                                        <i class="fa-solid fa-chevron-down text-muted" style="font-size: 0.7rem; font-weight: 900;"></i>
                                    </span>
                                </button>
                                <div class="collapse mt-2 px-3" id="faq11">
                                    <div class="card card-body border-0 bg-transparent text-muted small fw-light">Yes, TMS can be safely combined with medication.</div>
                                </div>
                            </div>
                        </div>

                        <!-- Category 4 -->
                        <p class="text-uppercase x-small fw-bold mb-3 ls-1" style="color: #c25e28;">MAINTENANCE, ACCESS, AND CHOOSING HARMONY</p>
                        <div class="accordion" id="accordionTMSRight2">
                            <!-- Q12 -->
                            <div class="mb-3">
                                <button class="btn w-100 text-start py-3 px-4 rounded-pill shadow-sm d-flex justify-content-between align-items-center fw-bold text-dark small border-0" type="button" data-bs-toggle="collapse" data-bs-target="#faq12" style="background-color: #E1E0D7;">
                                    Can I Come Back for More TMS? 
                                    <span class="bg-white rounded-circle d-flex align-items-center justify-content-center shadow-sm" style="width: 24px; height: 24px;">
                                        <i class="fa-solid fa-chevron-down text-muted" style="font-size: 0.7rem; font-weight: 900;"></i>
                                    </span>
                                </button>
                                <div class="collapse mt-2 px-3" id="faq12">
                                    <div class="card card-body border-0 bg-transparent text-muted small fw-light">Yes, booster or maintenance sessions are available if symptoms return.</div>
                                </div>
                            </div>
                            <!-- Q13 -->
                            <div class="mb-3">
                                <button class="btn w-100 text-start py-3 px-4 rounded-pill shadow-sm d-flex justify-content-between align-items-center fw-bold text-dark small border-0" type="button" data-bs-toggle="collapse" data-bs-target="#faq13" style="background-color: #E1E0D7;">
                                    Can TMS be part of a larger treatment plan? 
                                    <span class="bg-white rounded-circle d-flex align-items-center justify-content-center shadow-sm" style="width: 24px; height: 24px;">
                                        <i class="fa-solid fa-chevron-down text-muted" style="font-size: 0.7rem; font-weight: 900;"></i>
                                    </span>
                                </button>
                                <div class="collapse mt-2 px-3" id="faq13">
                                    <div class="card card-body border-0 bg-transparent text-muted small fw-light">Absolutely. It works well alongside therapy, psychiatry, and lifestyle changes.</div>
                                </div>
                            </div>
                            <!-- Q14 -->
                            <div class="mb-3">
                                <button class="btn w-100 text-start py-3 px-4 rounded-pill shadow-sm d-flex justify-content-between align-items-center fw-bold text-dark small border-0" type="button" data-bs-toggle="collapse" data-bs-target="#faq14" style="background-color: #E1E0D7;">
                                    What Does the Investment Look Like? 
                                    <span class="bg-white rounded-circle d-flex align-items-center justify-content-center shadow-sm" style="width: 24px; height: 24px;">
                                        <i class="fa-solid fa-chevron-down text-muted" style="font-size: 0.7rem; font-weight: 900;"></i>
                                    </span>
                                </button>
                                <div class="collapse mt-2 px-3" id="faq14">
                                    <div class="card card-body border-0 bg-transparent text-muted small fw-light">Using insurance significantly reduces the cost. We also check benefits for you.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    """

pattern = re.compile(rf"{re.escape(start_tag)}.*?{re.escape(end_tag)}", re.DOTALL)
content = pattern.sub(new_faq_html + end_tag, content)

with open(html_file, "w") as f:
    f.write(content)

print("FAQ updated successfully!")
