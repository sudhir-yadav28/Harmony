#!/usr/bin/env python3
"""Expand text content in the first two image sections of all condition pages."""

# Each entry: (filename, old_text, new_text)
replacements = [
    # ===== DEPRESSION =====
    ("depression.html",
     """<p class="text-muted lh-lg mb-4">Depression is more than just feeling sad; it can physically and
                        emotionally drain you, making everyday tasks feel impossible. At Harmony Neurocare, we
                        understand that traditional treatments don't work for everyone.</p>
                    <p class="text-muted lh-lg">We offer a range of advanced, evidence-based therapies designed to
                        target the root causes of depression and provide a safe, non-judgmental space to help you heal.
                    </p>""",
     """<p class="text-muted lh-lg mb-4">Depression is more than just feeling sad—it is a complex neurological condition that can physically and emotionally drain you, making everyday tasks feel impossible. You may struggle to get out of bed, lose interest in things you once loved, or feel an unshakable heaviness that colors every aspect of your life. At Harmony Neurocare, we understand that traditional treatments don't work for everyone, and that's why we specialize in advanced alternatives.</p>
                    <p class="text-muted lh-lg mb-4">Our team recognizes that depression affects each person differently. Whether you've been battling treatment-resistant depression for years or are experiencing a major depressive episode for the first time, we meet you exactly where you are.</p>
                    <p class="text-muted lh-lg">We offer a range of advanced, evidence-based therapies designed to target the root neurological causes of depression—not just manage symptoms—and provide a safe, compassionate, non-judgmental space to help you truly heal and reclaim your life.</p>"""),
    ("depression.html",
     """<p class="text-muted lh-lg">Major depression is often linked to underactive regions in the brain.
                        BrainsWay Deep TMS uses gentle magnetic pulses to stimulate these specific areas, restoring
                        balance and lifting the heavy fog of depression without systemic side effects.</p>""",
     """<p class="text-muted lh-lg mb-4">Major depression is often linked to underactive regions in the prefrontal cortex—the area responsible for mood regulation, motivation, and emotional processing. When these circuits become sluggish, the result is the persistent sadness, fatigue, and cognitive fog that characterize depression.</p>
                    <p class="text-muted lh-lg">BrainsWay Deep TMS uses patented H-coil technology to send gentle magnetic pulses deep into these specific brain regions, reactivating dormant neural pathways and restoring healthy communication between brain circuits. Unlike medication, TMS works directly at the source without systemic side effects, and most patients begin noticing improvement within the first few weeks of treatment.</p>"""),

    # ===== ANXIETY =====
    ("anxiety.html",
     """<p class="text-muted lh-lg mb-4">Anxiety is more than just feeling stressed—it is a pervasive sense
                        of fear and constant worry that can completely overwhelm your daily life. At Harmony Neurocare,
                        we understand how paralyzing severe anxiety can be.</p>
                    <p class="text-muted lh-lg">We offer specialized anxiety treatment plans designed to ease your
                        symptoms, calm your nervous system, and help you regain the confidence you need to move forward
                        safely.</p>""",
     """<p class="text-muted lh-lg mb-4">Anxiety is more than just feeling stressed—it is a pervasive, relentless sense of fear and constant worry that can completely overwhelm your daily life. Your heart races without reason, your mind spirals through worst-case scenarios, and even simple decisions feel paralyzing. At Harmony Neurocare, we understand how debilitating severe anxiety can be and how it robs you of the life you deserve.</p>
                    <p class="text-muted lh-lg mb-4">Living with chronic anxiety often means avoiding situations, relationships, and opportunities that could bring you joy. The physical toll—muscle tension, headaches, digestive issues, and chronic fatigue—can be just as exhausting as the mental burden.</p>
                    <p class="text-muted lh-lg">We offer specialized anxiety treatment plans that go beyond traditional approaches, designed to ease your symptoms at the neurological level, calm your overactive nervous system, and help you regain the confidence and inner peace you need to move forward safely.</p>"""),
    ("anxiety.html",
     """<p class="text-muted lh-lg">Severe anxiety is often linked to hyperactive regions in the brain.
                        BrainsWay Deep TMS uses gentle magnetic pulses to target these specific areas, restoring balance
                        and easing the constant feeling of dread without the systemic side effects of sedatives.</p>""",
     """<p class="text-muted lh-lg mb-4">Severe anxiety is often linked to hyperactive regions in the brain, particularly the amygdala and prefrontal cortex. When these areas misfire, your brain's natural threat-detection system gets stuck in overdrive, flooding your body with stress hormones and keeping you in a constant state of fight-or-flight.</p>
                    <p class="text-muted lh-lg">BrainsWay Deep TMS uses precisely targeted magnetic pulses to calm these overactive brain circuits, restoring the natural balance between alertness and relaxation. Unlike sedatives or benzodiazepines, TMS doesn't mask your anxiety—it addresses the root cause, easing the constant feeling of dread while keeping you fully alert and engaged in your daily life.</p>"""),

    # ===== PTSD =====
    ("ptsd.html",
     """<p class="text-muted lh-lg mb-4">Post-Traumatic Stress Disorder (PTSD) and trauma can trap you in
                        the past. When you are constantly struggling with flashbacks, nightmares, and severe
                        hypervigilance, your nervous system remains stuck in survival mode. At Harmony Neurocare, we
                        understand that traditional talk therapy alone isn't always enough to heal deep psychological
                        wounds.</p>
                    <p class="text-muted lh-lg">We offer trauma-informed treatments designed specifically to help you
                        safely process the past, dramatically reduce your physical and emotional symptoms, and finally
                        regain a sense of peace in your life.</p>""",
     """<p class="text-muted lh-lg mb-4">Post-Traumatic Stress Disorder (PTSD) and trauma can trap you in the past, making it feel impossible to move forward. When you are constantly struggling with vivid flashbacks, terrifying nightmares, and severe hypervigilance, your nervous system remains locked in survival mode—even when you are objectively safe. The world feels dangerous, trust feels impossible, and every unexpected sound or sensation can trigger an overwhelming emotional response.</p>
                    <p class="text-muted lh-lg mb-4">At Harmony Neurocare, we understand that traditional talk therapy alone isn't always enough to heal deep psychological wounds. Trauma physically changes the brain, and effective treatment often needs to address these neurological changes directly.</p>
                    <p class="text-muted lh-lg">We offer trauma-informed, neuroscience-backed treatments designed specifically to help you safely process the past, dramatically reduce your physical and emotional symptoms, and finally regain a sense of peace, safety, and control in your life.</p>"""),
    ("ptsd.html",
     """<p class="text-muted lh-lg">Ketamine therapy has shown profound potential in treating severe PTSD
                        and trauma. By fostering neuroplasticity, it allows the brain to form new pathways and detach
                        intense emotional responses from traumatic memories, offering a gentle way to process the past
                        and reduce the grip of flashbacks and nightmares.</p>""",
     """<p class="text-muted lh-lg mb-4">Ketamine therapy has shown profound and groundbreaking potential in treating severe PTSD and trauma. Traditional PTSD medications can take weeks to show effects and often only partially reduce symptoms. Ketamine works differently—by fostering neuroplasticity, it allows the brain to rapidly form new neural pathways and begin to detach intense emotional responses from traumatic memories.</p>
                    <p class="text-muted lh-lg">This means that the overwhelming fear, panic, and emotional flooding that accompany flashbacks and nightmares can be significantly reduced, offering a gentler, faster way to process the past. Many patients report feeling meaningful relief within their first few sessions, finally experiencing moments of genuine calm and safety.</p>"""),

    # ===== OCD =====
    ("ocd.html",
     """<p class="text-muted lh-lg mb-4">Obsessive-Compulsive Disorder (OCD) can make you feel like a
                        prisoner in your own mind. When intrusive thoughts and exhausting, repetitive rituals dictate
                        your daily schedule, it is incredibly difficult to live a normal life. At Harmony Neurocare, we
                        understand the immense toll that severe OCD takes on your wellbeing.</p>
                    <p class="text-muted lh-lg">Our dedicated OCD treatments go beyond standard talk therapy to target
                        the specific neural pathways responsible for obsessive behaviors, helping you break the cycle of
                        compulsions and finally regain control of your life.</p>""",
     """<p class="text-muted lh-lg mb-4">Obsessive-Compulsive Disorder (OCD) can make you feel like a prisoner in your own mind. When intrusive, unwanted thoughts bombard you relentlessly and exhausting, repetitive rituals dictate your entire daily schedule, it is incredibly difficult to live a normal life. You may spend hours each day trapped in compulsive loops—checking, counting, cleaning, or arranging—knowing the behavior is irrational but feeling powerless to stop.</p>
                    <p class="text-muted lh-lg mb-4">At Harmony Neurocare, we understand the immense toll that severe OCD takes on your wellbeing, your relationships, and your ability to function. We also know that many patients have tried medication and therapy without finding adequate relief.</p>
                    <p class="text-muted lh-lg">Our dedicated OCD treatments go beyond standard approaches to target the specific neural pathways in the brain responsible for obsessive thought patterns and compulsive behaviors, helping you break the cycle and finally regain control of your life.</p>"""),
    ("ocd.html",
     """<p class="text-muted lh-lg">BrainsWay Deep TMS is one of the only FDA-cleared, non-invasive
                        therapies specifically designed for OCD. By directing magnetic pulses deep into the anterior
                        cingulate cortex—the region responsible for obsessive loops—this technology actively helps quiet
                        intrusive thoughts and reduces the urge to perform rituals, all without the side effects of
                        medications.</p>""",
     """<p class="text-muted lh-lg mb-4">BrainsWay Deep TMS is one of the only FDA-cleared, non-invasive therapies specifically designed and approved for OCD treatment. Unlike standard TMS, BrainsWay's patented H-coil technology can reach deeper brain structures that are inaccessible to traditional surface-level magnetic stimulation.</p>
                    <p class="text-muted lh-lg">By directing precise magnetic pulses deep into the anterior cingulate cortex and medial prefrontal cortex—the regions directly responsible for generating obsessive thought loops and compulsive urges—this technology actively helps quiet intrusive thoughts and significantly reduces the overwhelming need to perform rituals. The treatment is well-tolerated, requires no anesthesia, and works without the weight gain, sexual dysfunction, or cognitive dulling often associated with OCD medications.</p>"""),

    # ===== BIPOLAR =====
    ("bipolar.html",
     """<p class="text-muted lh-lg mb-4">Bipolar disorder can create profound instability, pulling you
                        between emotional extremes that exhaust you and disrupt your life. We know how difficult it is
                        to live with severe mood swings, from the depths of depression to the heights of mania or
                        hypomania.</p>
                    <p class="text-muted lh-lg">Our expert psychiatric care is focused on more than just symptom
                        management. We help you establish long-term mental and emotional balance so that you can
                        navigate your life with predictability, confidence, and inner peace.</p>""",
     """<p class="text-muted lh-lg mb-4">Bipolar disorder can create profound instability, pulling you between emotional extremes that exhaust you and disrupt every aspect of your life. The crushing lows of depression leave you unable to function, while the highs of mania or hypomania can lead to impulsive decisions, strained relationships, and consequences that follow you long after the episode ends.</p>
                    <p class="text-muted lh-lg mb-4">We know how difficult it is to live with severe mood swings—the unpredictability, the fear of the next episode, and the toll it takes on your career, family, and sense of self. Many patients feel misunderstood or frustrated by treatments that flatten their emotions without truly stabilizing them.</p>
                    <p class="text-muted lh-lg">Our expert psychiatric care is focused on more than just symptom management. We take a comprehensive, personalized approach to help you establish long-term mental and emotional balance, so you can navigate your life with predictability, confidence, and genuine inner peace—without losing what makes you uniquely you.</p>"""),
    ("bipolar.html",
     """<p class="text-muted lh-lg">Treating bipolar disorder requires a highly nuanced approach to
                        medication and therapy. Our psychiatric providers specialize in finding the precise combinations
                        needed to prevent future mood episodes, protect your cognitive health, and maintain emotional
                        equilibrium over the long term, without flattening your personality.</p>""",
     """<p class="text-muted lh-lg mb-4">Treating bipolar disorder requires a highly nuanced, individualized approach to medication and therapy. Unlike depression or anxiety, bipolar disorder demands careful calibration—the wrong medication or dosage can actually trigger manic episodes or worsen symptoms. That's why expertise matters.</p>
                    <p class="text-muted lh-lg">Our psychiatric providers specialize in the complex pharmacology of mood stabilizers, atypical antipsychotics, and adjunctive therapies. We work closely with you to find the precise combinations needed to prevent future mood episodes, protect your cognitive health, and maintain lasting emotional equilibrium—all without flattening your personality, creativity, or drive.</p>"""),

    # ===== ADHD =====
    ("adhd.html",
     """<p class="text-muted lh-lg mb-4">Attention-Deficit/Hyperactivity Disorder (ADHD) and ADD can make
                        every day feel chaotic. When you are constantly struggling with focus, restlessness, or
                        impulsivity, even simple tasks can feel frustrating and insurmountable. At Harmony Neurocare, we
                        understand how a neurodivergent brain operates.</p>
                    <p class="text-muted lh-lg">We offer personalized treatment plans designed to help you build
                        necessary structure, manage executive dysfunction, and regain control over your attention so you
                        can thrive in your personal and professional life.</p>""",
     """<p class="text-muted lh-lg mb-4">Attention-Deficit/Hyperactivity Disorder (ADHD) and ADD can make every day feel chaotic and overwhelming. When you are constantly struggling with focus, restlessness, or impulsivity, even simple tasks can feel frustrating and insurmountable. You may feel like you're always running behind, forgetting important things, or unable to follow through despite your best intentions.</p>
                    <p class="text-muted lh-lg mb-4">At Harmony Neurocare, we understand how a neurodivergent brain operates. ADHD is not a character flaw or a lack of willpower—it is a neurological condition rooted in differences in brain chemistry and executive function. Adults with ADHD often struggle silently for years, developing coping mechanisms that mask the underlying condition while creating anxiety, depression, and burnout.</p>
                    <p class="text-muted lh-lg">We offer personalized treatment plans designed to help you build necessary structure, manage executive dysfunction, and regain control over your attention so you can thrive in your personal and professional life—without sacrificing your creativity or energy.</p>"""),
    ("adhd.html",
     """<p class="text-muted lh-lg">Managing ADD/ADHD effectively often starts with finding the right
                        medication to quiet a noisy mind. Our psychiatric team works closely with you to find treatments
                        that improve your attention, decrease impulsivity, and help build a reliable foundation without
                        blunting your natural creativity or energy.</p>""",
     """<p class="text-muted lh-lg mb-4">Managing ADD/ADHD effectively often starts with finding the right medication to quiet a noisy mind and sharpen your focus. But effective treatment goes far beyond simply prescribing stimulants. Our psychiatric team takes the time to understand your unique presentation—whether you're primarily inattentive, hyperactive-impulsive, or a combination of both.</p>
                    <p class="text-muted lh-lg">We work closely with you to find treatments that genuinely improve your attention, decrease impulsivity, and help build a reliable cognitive foundation. We also monitor for and address the common co-occurring conditions like anxiety and depression that often accompany ADHD, ensuring a holistic approach that supports your complete mental health—without blunting your natural creativity, personality, or drive.</p>"""),

    # ===== SUICIDAL IDEATION =====
    ("suicidal-ideation.html",
     """<p class="text-muted lh-lg mb-4">When you are feeling hopeless or like there's no way out, the pain
                        can feel entirely isolating. Suicidal ideation is a sign of immense psychological distress, but
                        it is deeply important to know that you are not alone, and these feelings do not have to be
                        permanent.</p>
                    <p class="text-muted lh-lg">At Harmony Neurocare, we provide a safe, compassionate, and stigma-free
                        environment. We offer rapid-relief treatments designed to quickly alleviate the intensity of
                        these hopeless feelings so you can find renewed purpose and the strength to heal.</p>""",
     """<p class="text-muted lh-lg mb-4">When you are feeling hopeless or like there's no way out, the pain can feel entirely isolating and all-consuming. Every day becomes a struggle to simply exist, and the weight of despair can make it seem like things will never improve. Suicidal ideation is a sign of immense psychological distress, but it is deeply important to know that you are not alone, and these feelings—as overwhelming as they are—do not have to be permanent.</p>
                    <p class="text-muted lh-lg mb-4">We understand that reaching out for help in these moments takes extraordinary courage. Many people suffering from suicidal thoughts feel ashamed or afraid to speak up, worried about being judged or misunderstood. That fear should never stand between you and the care you need.</p>
                    <p class="text-muted lh-lg">At Harmony Neurocare, we provide a safe, deeply compassionate, and completely stigma-free environment. We offer rapid-relief treatments—some FDA-approved specifically for this purpose—designed to quickly alleviate the intensity of hopeless feelings so you can find renewed purpose, reconnect with the people who love you, and discover the strength to heal.</p>"""),
    ("suicidal-ideation.html",
     """<p class="text-muted lh-lg">When you are in immediate distress, waiting weeks for oral
                        antidepressants to work is not an option. SPRAVATO® (esketamine) is an FDA-approved nasal spray
                        that explicitly treats depressive symptoms in adults with Major Depressive Disorder accompanied
                        by suicidal thoughts or actions, offering rapid relief often within hours or days.</p>""",
     """<p class="text-muted lh-lg mb-4">When you are in immediate distress, waiting weeks or months for oral antidepressants to take effect is simply not an option. Every day matters, and rapid intervention can be life-saving. That's why we offer SPRAVATO® (esketamine)—the only FDA-approved nasal spray specifically designed to treat depressive symptoms in adults with Major Depressive Disorder accompanied by suicidal thoughts or actions.</p>
                    <p class="text-muted lh-lg">Unlike traditional antidepressants that can take 4-6 weeks to show results, SPRAVATO® works through a completely different mechanism, offering measurable relief often within hours or days. Treatment is administered in our safe, supervised clinical setting, where you are monitored and supported throughout the entire process. For many patients, this rapid response provides the critical bridge they need to stabilize and begin their journey toward lasting recovery.</p>"""),

    # ===== TRAUMA & ADDICTION =====
    ("trauma-addiction.html",
     """<p class="text-muted lh-lg mb-4">Living with the interconnected effects of trauma or addiction can
                        make every day feel like a battle for survival. These deeply ingrained cycles often go
                        hand-in-hand, physically and emotionally draining you until simply existing feels impossible.
                    </p>
                    <p class="text-muted lh-lg">At Harmony Neurocare, we provide compassionate, evidence-based care that
                        targets the neurological roots of these conditions. Our goal is to drastically reduce your
                        symptoms and restore the stability you need to build a lasting foundation for healing.</p>""",
     """<p class="text-muted lh-lg mb-4">Living with the interconnected effects of trauma and addiction can make every day feel like a battle for survival. These deeply ingrained cycles often go hand-in-hand—unresolved trauma frequently drives substance use as a coping mechanism, while addiction creates its own layer of trauma, shame, and neurological damage. The result is a devastating cycle that physically and emotionally drains you until simply existing feels impossible.</p>
                    <p class="text-muted lh-lg mb-4">Many people struggling with co-occurring trauma and addiction feel trapped, having tried traditional rehabilitation programs that address one condition but not the other. True recovery requires treating both simultaneously, at the neurological level where these conditions are deeply intertwined.</p>
                    <p class="text-muted lh-lg">At Harmony Neurocare, we provide compassionate, evidence-based care that targets the neurological roots of both trauma and addictive behaviors. Our goal is to drastically reduce your symptoms, break the cycle of self-medication, and restore the stability you need to build a lasting, sustainable foundation for genuine healing and recovery.</p>"""),
    ("trauma-addiction.html",
     """<p class="text-muted lh-lg">Overcoming trauma and addiction requires more than just willpower; it
                        requires specialized psychiatric support to manage withdrawal, cravings, and trauma responses.
                        We utilize advanced medication management and therapies to help stabilize your nervous system
                        and rewire the pathways that keep you stuck, offering a comprehensive path to recovery.</p>""",
     """<p class="text-muted lh-lg mb-4">Overcoming trauma and addiction requires more than just willpower or determination; it requires specialized psychiatric support that understands the complex interplay between traumatic stress responses and addictive behavior patterns. Your brain has physically adapted to both the trauma and the substance use, creating deeply ingrained neural pathways that drive cravings, avoidance, and emotional reactivity.</p>
                    <p class="text-muted lh-lg">We utilize advanced medication management, targeted therapies, and cutting-edge neurostimulation techniques to help stabilize your dysregulated nervous system and actively rewire the neural pathways that keep you stuck in destructive cycles. This comprehensive, dual-focused approach addresses both the trauma and the addiction simultaneously, offering a truly integrated path to lasting recovery and renewed stability.</p>"""),
]

import os
os.chdir("/Users/sudhiryadav/Downloads/harmony-replica")

for filename, old_text, new_text in replacements:
    with open(filename, "r") as f:
        content = f.read()

    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(filename, "w") as f:
            f.write(content)
        print(f"✅ Updated section in {filename}")
    else:
        print(f"❌ Text not found in {filename}")

print("\nDone! All sections expanded.")
