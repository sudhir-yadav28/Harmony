#!/usr/bin/env python3
"""Add Signs & Symptoms + Treatment Options sections to all condition pages."""

import re

# Define condition-specific content
conditions = {
    "depression.html": {
        "symptoms_title": "Recognizing the Signs of Depression",
        "symptoms_subtitle": "COMMON SYMPTOMS WE TREAT",
        "symptoms": [
            {"icon": "fa-cloud-rain", "title": "Persistent Sadness", "desc": "A deep, unshakable feeling of emptiness or hopelessness that lasts for weeks or months."},
            {"icon": "fa-bed", "title": "Sleep Disruption", "desc": "Sleeping too much or struggling with insomnia, leaving you exhausted regardless."},
            {"icon": "fa-brain", "title": "Difficulty Concentrating", "desc": "A heavy mental fog that makes it hard to think clearly, make decisions, or remember things."},
            {"icon": "fa-battery-quarter", "title": "Fatigue & Low Energy", "desc": "Feeling physically drained and lacking the motivation to engage in activities you once enjoyed."},
            {"icon": "fa-utensils", "title": "Appetite Changes", "desc": "Significant weight loss or gain due to changes in appetite and eating patterns."},
            {"icon": "fa-heart-crack", "title": "Loss of Interest", "desc": "Withdrawing from hobbies, social activities, and relationships that once brought you joy."},
        ],
        "treatments": [
            {"icon": "fa-magnet", "title": "Deep TMS Therapy", "desc": "FDA-cleared magnetic stimulation that targets underactive brain regions linked to depression, often effective when medications fail.", "link": "tms.html"},
            {"icon": "fa-spray-can-sparkles", "title": "Ketamine & SPRAVATO®", "desc": "Rapid-acting treatments that can provide relief from severe depressive symptoms within hours, not weeks.", "link": "ketamine.html"},
            {"icon": "fa-pills", "title": "Psychiatric Care", "desc": "Expert medication management and personalized treatment plans tailored to your unique brain chemistry.", "link": "psychiatry.html"},
        ],
    },
    "anxiety.html": {
        "symptoms_title": "Recognizing the Signs of Anxiety",
        "symptoms_subtitle": "COMMON SYMPTOMS WE TREAT",
        "symptoms": [
            {"icon": "fa-heart-pulse", "title": "Racing Heart", "desc": "Persistent heart palpitations, chest tightness, or shortness of breath even without physical activity."},
            {"icon": "fa-bolt", "title": "Constant Worry", "desc": "An overwhelming sense of dread or fear about everyday situations that feels impossible to control."},
            {"icon": "fa-person-running", "title": "Restlessness", "desc": "Feeling on edge, unable to sit still, or an internal sense of nervous energy that won't quiet down."},
            {"icon": "fa-moon", "title": "Sleep Problems", "desc": "Difficulty falling or staying asleep due to racing thoughts and an inability to relax at night."},
            {"icon": "fa-hand-holding-medical", "title": "Physical Symptoms", "desc": "Muscle tension, headaches, stomach issues, and trembling that accompany your emotional distress."},
            {"icon": "fa-people-arrows", "title": "Social Avoidance", "desc": "Withdrawing from social situations, work, or daily activities out of fear of judgment or panic attacks."},
        ],
        "treatments": [
            {"icon": "fa-magnet", "title": "Deep TMS Therapy", "desc": "Targets hyperactive brain regions responsible for anxious thoughts, calming worry responses without sedating side effects.", "link": "tms.html"},
            {"icon": "fa-spray-can-sparkles", "title": "Ketamine Therapy", "desc": "Promotes neuroplasticity and can rapidly ease severe anxiety symptoms, helping you feel relief much faster.", "link": "ketamine.html"},
            {"icon": "fa-pills", "title": "Psychiatric Care", "desc": "Careful medication management to find the right balance that controls anxiety without numbing your personality.", "link": "psychiatry.html"},
        ],
    },
    "ptsd.html": {
        "symptoms_title": "Recognizing the Signs of PTSD",
        "symptoms_subtitle": "COMMON SYMPTOMS WE TREAT",
        "symptoms": [
            {"icon": "fa-film", "title": "Flashbacks", "desc": "Vivid, intrusive re-experiencing of the traumatic event that feels as though it is happening all over again."},
            {"icon": "fa-moon", "title": "Nightmares", "desc": "Disturbing dreams related to the trauma that disrupt your sleep and leave you exhausted and afraid."},
            {"icon": "fa-shield-halved", "title": "Hypervigilance", "desc": "Being constantly on guard, easily startled, and unable to relax even in safe environments."},
            {"icon": "fa-face-grimace", "title": "Emotional Numbing", "desc": "Feeling detached from others and the world, as if you're going through the motions without truly living."},
            {"icon": "fa-ban", "title": "Avoidance", "desc": "Going to great lengths to avoid places, people, or situations that remind you of the trauma."},
            {"icon": "fa-burst", "title": "Irritability & Anger", "desc": "Sudden outbursts of anger, difficulty controlling emotions, and feeling on edge without clear triggers."},
        ],
        "treatments": [
            {"icon": "fa-magnet", "title": "Deep TMS Therapy", "desc": "Targets the brain's fear and memory centers to help reduce the intensity of trauma responses and flashbacks.", "link": "tms.html"},
            {"icon": "fa-spray-can-sparkles", "title": "Ketamine Therapy", "desc": "Fosters neuroplasticity to help the brain form new pathways, detaching intense emotional responses from traumatic memories.", "link": "ketamine.html"},
            {"icon": "fa-pills", "title": "Psychiatric Care", "desc": "Specialized medication management to stabilize your nervous system and reduce hypervigilance and emotional reactivity.", "link": "psychiatry.html"},
        ],
    },
    "ocd.html": {
        "symptoms_title": "Recognizing the Signs of OCD",
        "symptoms_subtitle": "COMMON SYMPTOMS WE TREAT",
        "symptoms": [
            {"icon": "fa-rotate", "title": "Repetitive Rituals", "desc": "Compulsive behaviors like excessive hand-washing, checking, or counting that you feel driven to repeat."},
            {"icon": "fa-brain", "title": "Intrusive Thoughts", "desc": "Unwanted, disturbing thoughts or images that cause intense anxiety and are difficult to dismiss."},
            {"icon": "fa-clock", "title": "Time-Consuming Routines", "desc": "Spending hours each day on rituals that interfere with your work, relationships, and daily life."},
            {"icon": "fa-triangle-exclamation", "title": "Fear of Contamination", "desc": "Overwhelming worry about germs, dirt, or illness that leads to compulsive cleaning and avoidance."},
            {"icon": "fa-arrows-left-right", "title": "Need for Symmetry", "desc": "An intense need to have things arranged perfectly or in a particular order, causing significant distress."},
            {"icon": "fa-lock", "title": "Doubt & Checking", "desc": "Persistent doubt about whether you've completed tasks correctly, leading to repeated checking behaviors."},
        ],
        "treatments": [
            {"icon": "fa-magnet", "title": "Deep TMS Therapy", "desc": "The only FDA-cleared non-invasive treatment specifically for OCD, targeting the anterior cingulate cortex to quiet obsessive loops.", "link": "tms.html"},
            {"icon": "fa-spray-can-sparkles", "title": "Ketamine Therapy", "desc": "Can help break rigid thought patterns by promoting neuroplasticity, offering a new approach to treatment-resistant OCD.", "link": "ketamine.html"},
            {"icon": "fa-pills", "title": "Psychiatric Care", "desc": "Expert medication management using SSRIs and other agents specifically effective for managing OCD symptoms.", "link": "psychiatry.html"},
        ],
    },
    "bipolar.html": {
        "symptoms_title": "Recognizing the Signs of Bipolar Disorder",
        "symptoms_subtitle": "COMMON SYMPTOMS WE TREAT",
        "symptoms": [
            {"icon": "fa-arrows-up-down", "title": "Mood Swings", "desc": "Extreme shifts between emotional highs (mania) and devastating lows (depression) that disrupt your stability."},
            {"icon": "fa-bolt-lightning", "title": "Manic Episodes", "desc": "Periods of elevated energy, racing thoughts, impulsive decisions, and a decreased need for sleep."},
            {"icon": "fa-cloud-rain", "title": "Depressive Episodes", "desc": "Crushing sadness, fatigue, hopelessness, and withdrawal that can last for weeks or months."},
            {"icon": "fa-bed", "title": "Sleep Disruption", "desc": "Dramatic changes in sleep patterns—from barely sleeping during mania to sleeping excessively during depression."},
            {"icon": "fa-comments", "title": "Pressured Speech", "desc": "Talking rapidly, jumping between topics, and feeling a compulsive need to share every thought during manic phases."},
            {"icon": "fa-scale-unbalanced", "title": "Impulsive Behavior", "desc": "Risky decisions during manic episodes such as overspending, reckless driving, or impulsive lifestyle changes."},
        ],
        "treatments": [
            {"icon": "fa-magnet", "title": "Deep TMS Therapy", "desc": "Can be used as an adjunctive treatment for the depressive phase of bipolar disorder, helping stabilize mood regulation.", "link": "tms.html"},
            {"icon": "fa-spray-can-sparkles", "title": "Ketamine Therapy", "desc": "May provide rapid relief during severe bipolar depressive episodes when traditional medications are insufficient.", "link": "ketamine.html"},
            {"icon": "fa-pills", "title": "Psychiatric Care", "desc": "Specialized mood stabilizer management to prevent future episodes and maintain long-term emotional equilibrium.", "link": "psychiatry.html"},
        ],
    },
    "adhd.html": {
        "symptoms_title": "Recognizing the Signs of ADHD / ADD",
        "symptoms_subtitle": "COMMON SYMPTOMS WE TREAT",
        "symptoms": [
            {"icon": "fa-bullseye", "title": "Difficulty Focusing", "desc": "Struggling to maintain attention on tasks, conversations, or reading, even when you genuinely want to concentrate."},
            {"icon": "fa-shuffle", "title": "Disorganization", "desc": "Chronic difficulty with planning, prioritizing, and keeping track of tasks, appointments, and belongings."},
            {"icon": "fa-forward-fast", "title": "Impulsivity", "desc": "Acting without thinking, interrupting others, or making hasty decisions that you later regret."},
            {"icon": "fa-person-running", "title": "Restlessness", "desc": "An internal sense of restlessness or the need to be constantly moving, fidgeting, or tapping."},
            {"icon": "fa-hourglass-half", "title": "Time Blindness", "desc": "Severely underestimating how long tasks will take, leading to chronic lateness and missed deadlines."},
            {"icon": "fa-head-side-virus", "title": "Emotional Dysregulation", "desc": "Intense emotional reactions, frustration, and difficulty managing feelings in proportion to the situation."},
        ],
        "treatments": [
            {"icon": "fa-magnet", "title": "Deep TMS Therapy", "desc": "Emerging research supports TMS for improving focus and executive function by stimulating underactive prefrontal regions.", "link": "tms.html"},
            {"icon": "fa-spray-can-sparkles", "title": "Ketamine Therapy", "desc": "May help address co-occurring depression and anxiety that often accompany ADHD, improving overall mental health.", "link": "ketamine.html"},
            {"icon": "fa-pills", "title": "Psychiatric Care", "desc": "Careful stimulant and non-stimulant medication management to improve focus, reduce impulsivity, and build structure.", "link": "psychiatry.html"},
        ],
    },
    "suicidal-ideation.html": {
        "symptoms_title": "Warning Signs to Take Seriously",
        "symptoms_subtitle": "RECOGNIZING WHEN SOMEONE NEEDS HELP",
        "symptoms": [
            {"icon": "fa-comment-slash", "title": "Talking About Death", "desc": "Expressing thoughts about wanting to die, being a burden to others, or feeling trapped with no way out."},
            {"icon": "fa-people-arrows", "title": "Social Withdrawal", "desc": "Suddenly pulling away from family, friends, and activities, or saying goodbye in unusual ways."},
            {"icon": "fa-face-sad-tear", "title": "Hopelessness", "desc": "Expressing a profound belief that things will never get better and that there is no reason to go on."},
            {"icon": "fa-arrows-up-down", "title": "Mood Changes", "desc": "Dramatic mood shifts—sudden calm after a period of depression can sometimes indicate a decision has been made."},
            {"icon": "fa-shield-halved", "title": "Reckless Behavior", "desc": "Engaging in dangerous activities without concern for consequences, as though life no longer matters."},
            {"icon": "fa-box-open", "title": "Giving Away Possessions", "desc": "Distributing valued belongings or making arrangements as if preparing for the end."},
        ],
        "treatments": [
            {"icon": "fa-spray-can-sparkles", "title": "SPRAVATO® (Esketamine)", "desc": "The only FDA-approved nasal spray for adults with MDD and suicidal thoughts, offering rapid relief within hours.", "link": "ketamine.html"},
            {"icon": "fa-magnet", "title": "Deep TMS Therapy", "desc": "Targets brain regions involved in mood regulation to help lift the weight of severe depression and hopelessness.", "link": "tms.html"},
            {"icon": "fa-pills", "title": "Psychiatric Crisis Care", "desc": "Immediate, compassionate psychiatric intervention with medication adjustments to stabilize acute distress.", "link": "psychiatry.html"},
        ],
    },
    "trauma-addiction.html": {
        "symptoms_title": "Recognizing the Signs of Trauma & Addiction",
        "symptoms_subtitle": "COMMON SYMPTOMS WE TREAT",
        "symptoms": [
            {"icon": "fa-wine-bottle", "title": "Substance Dependence", "desc": "Using alcohol, drugs, or other substances as a way to cope with emotional pain and escape traumatic memories."},
            {"icon": "fa-film", "title": "Flashbacks & Triggers", "desc": "Re-experiencing traumatic events when exposed to certain sights, sounds, smells, or situations."},
            {"icon": "fa-face-grimace", "title": "Emotional Numbness", "desc": "Feeling disconnected from yourself and others, unable to experience joy or form meaningful bonds."},
            {"icon": "fa-rotate-left", "title": "Relapse Cycles", "desc": "Repeated attempts to quit substance use followed by relapse, often triggered by unresolved trauma."},
            {"icon": "fa-bed", "title": "Sleep Disturbances", "desc": "Nightmares, insomnia, or substance-dependent sleep patterns that leave you perpetually exhausted."},
            {"icon": "fa-link-slash", "title": "Relationship Strain", "desc": "Difficulty maintaining healthy relationships due to trust issues, emotional volatility, or substance use."},
        ],
        "treatments": [
            {"icon": "fa-magnet", "title": "Deep TMS Therapy", "desc": "Targets brain circuits involved in both trauma responses and addictive behaviors, addressing the neurological root of both.", "link": "tms.html"},
            {"icon": "fa-spray-can-sparkles", "title": "Ketamine Therapy", "desc": "Promotes neuroplasticity to help rewire trauma-linked pathways and reduce cravings associated with substance use.", "link": "ketamine.html"},
            {"icon": "fa-pills", "title": "Psychiatric Care", "desc": "Comprehensive medication management for withdrawal, cravings, and co-occurring mental health conditions.", "link": "psychiatry.html"},
        ],
    },
}


def generate_symptoms_section(data):
    """Generate the Signs & Symptoms HTML section."""
    cards = ""
    for s in data["symptoms"]:
        cards += f"""
                <div class="col-md-6 col-lg-4">
                    <div class="d-flex align-items-start gap-3 p-4 bg-white rounded-4 shadow-sm h-100">
                        <div class="flex-shrink-0 d-flex align-items-center justify-content-center rounded-circle"
                            style="width: 50px; height: 50px; background-color: rgba(194, 94, 40, 0.1);">
                            <i class="fa-solid {s['icon']}" style="color: #c25e28; font-size: 1.1rem;"></i>
                        </div>
                        <div>
                            <h5 class="fw-bold mb-2" style="font-size: 1rem; color: #2A371E;">{s['title']}</h5>
                            <p class="text-muted mb-0" style="font-size: 0.88rem; line-height: 1.6;">{s['desc']}</p>
                        </div>
                    </div>
                </div>"""

    return f"""
    <!-- SIGNS & SYMPTOMS -->
    <section class="py-5 bg-white">
        <div class="container py-5">
            <div class="text-center mb-5">
                <p class="text-uppercase small fw-bold ls-1 mb-3" style="color: #c25e28;">{data['symptoms_subtitle']}</p>
                <h2 class="serif-font display-6 mb-3" style="color: #2A371E;">{data['symptoms_title']}</h2>
                <p class="text-muted mx-auto" style="max-width: 600px;">If you or a loved one is experiencing several of these symptoms, it may be time to seek professional support.</p>
            </div>
            <div class="row g-4">{cards}
            </div>
        </div>
    </section>
"""


def generate_treatments_section(data):
    """Generate the Treatment Options HTML section."""
    cards = ""
    for t in data["treatments"]:
        cards += f"""
                <div class="col-lg-4">
                    <div class="card border-0 rounded-5 shadow-sm h-100 overflow-hidden">
                        <div class="card-body p-4 p-lg-5 d-flex flex-column">
                            <div class="d-flex align-items-center justify-content-center rounded-circle mb-4"
                                style="width: 60px; height: 60px; background-color: #2A371E;">
                                <i class="fa-solid {t['icon']} text-white" style="font-size: 1.3rem;"></i>
                            </div>
                            <h4 class="serif-font mb-3" style="color: #2A371E;">{t['title']}</h4>
                            <p class="text-muted mb-4" style="font-size: 0.9rem; line-height: 1.7;">{t['desc']}</p>
                            <a href="{t['link']}" class="mt-auto text-decoration-none fw-bold small text-uppercase ls-1"
                                style="color: #c25e28; font-size: 0.75rem; letter-spacing: 1.5px;">LEARN MORE <i
                                    class="fa-solid fa-arrow-right ms-1" style="font-size: 0.65rem;"></i></a>
                        </div>
                    </div>
                </div>"""

    return f"""
    <!-- TREATMENT OPTIONS -->
    <section class="py-5" style="background-color: #F9F7F2;">
        <div class="container py-5">
            <div class="text-center mb-5">
                <p class="text-uppercase small fw-bold ls-1 mb-3" style="color: #c25e28;">HOW WE CAN HELP</p>
                <h2 class="serif-font display-6 mb-3" style="color: #2A371E;">Treatment Options at Harmony Neurocare</h2>
                <p class="text-muted mx-auto" style="max-width: 600px;">We offer a range of advanced, evidence-based therapies tailored to your unique needs.</p>
            </div>
            <div class="row g-4">{cards}
            </div>
        </div>
    </section>
"""


# Process each file
for filename, data in conditions.items():
    filepath = filename
    with open(filepath, "r") as f:
        content = f.read()

    symptoms_html = generate_symptoms_section(data)
    treatments_html = generate_treatments_section(data)

    # Insert before the CTA section
    cta_marker = "    <!-- CTA -->"
    if cta_marker in content:
        new_content = content.replace(
            cta_marker,
            symptoms_html + treatments_html + cta_marker
        )
        with open(filepath, "w") as f:
            f.write(new_content)
        print(f"✅ Updated {filename}")
    else:
        print(f"❌ CTA marker not found in {filename}")

print("\nDone! All condition pages updated.")
