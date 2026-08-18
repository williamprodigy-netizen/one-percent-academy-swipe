#!/usr/bin/env python3
"""Build the 1 Percent Academy (Jacqueline) swipe site.

Run: python3 build_site.py
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/1PERCENT_ACADEMY_Swipe")

CONFIG = {
    "SITE": "1 Percent Academy — Jacqueline",
    # must match the capture folder, which drops the parentheses from the
    # registry's creator name — extras.capture_dirs() globs on this verbatim
    "CREATOR": "1 Percent Academy Jacqueline",
    "FUNNEL_IDS": ["F120"],
    "CAPTURED": "3 August 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/1PERCENT_ACADEMY_Swipe",
    "BLURB": "Amazon FBA sold to women through a free &ldquo;live&rdquo; masterclass that is a "
             "recorded 1h42m file. Structurally this is UGC World in a different vertical. Two "
             "mechanics are worth taking: a money question on the registration form itself, and "
             "two entire pages built for nothing but show rate. The price is never stated "
             "anywhere &mdash; not on a page, not on a slide, not in 19,078 words of webinar.",

    "PAGES": [
        ("index.html", "Overview"),
        ("analysis.html", "Analysis"),
        ("pages.html", "Funnel pages"),
        ("copybank.html", "Copy bank"),
        ("webinar.html", "Webinar slides"),
        ("transcripts.html", "Transcripts"),
        ("videos.html", "Video library"),
        ("board.html", "Wired board"),
    ],

    "STATS": [
        ("Price", "never stated"),
        ("Webinar", "1h 42m 49s"),
        ("Words", "19,078"),
        ("Slides kept", "174"),
        ("Funnel pages", "9"),
        ("Opt-in variants", "4"),
        ("Budget bands", "5"),
        ("Show-rate pages", "2"),
    ],

    "OFFER": [
        ("Product", "1% Academy &mdash; Amazon FBA mentorship for women"),
        ("Mechanism", "&ldquo;The Premium Brand Method&rdquo; &mdash; buy low-cost products, "
                      "customise and brand them, rank on page 1"),
        ("Price", "<b>never stated</b>. Two costs are named &mdash; enrolment and inventory &mdash; "
                  "then blurred together and pushed to the call"),
        ("Capital framing", "&ldquo;Some women come in with $4,000, some come in with $10,000 "
                            "and we help both of them if we can&rdquo; (75:38)"),
        ("Application bands", "&lt;$5,000 &middot; $5&ndash;8k &middot; $8&ndash;12k &middot; "
                              "$12&ndash;15k &middot; $15,000+"),
        ("Time to first product", "4&ndash;5 months, stated in the FAQ"),
        ("Time commitment", "1&ndash;2 hours a day, &ldquo;2 hours maximum&rdquo;"),
        ("Bonuses", "Accountability coach, 100 vetted products, done-for-you listing creation, "
                    "3 weekly live calls, A&ndash;Z course lifetime access, China sourcing partners"),
        ("Scarcity bonus", "First 20 women get 3 months of the product-research software free, "
                           "framed as $1,100 of value at $97/mo"),
        ("Guarantee", "none offered. &ldquo;If you follow everything I outline it will work&rdquo;"),
    ],

    "FINDINGS": [
        ("The money question is on the registration form",
         "The opt-in form carries a required dropdown &mdash; <b>&ldquo;How much could you "
         "comfortably invest towards your Amazon Store Today?&rdquo;</b> with two options, "
         "Under $4,000 and $4,000+. It posts to a Zapier catch hook before WebinarJam ever sees "
         "the lead. They know a registrant's capital before she has watched a single minute. "
         "Caveat: the form is present in the markup of every variant but did not render on the "
         "live pages we captured, so treat it as their intent rather than their current state."),
        ("Two entire pages exist only to raise show rate",
         "Nothing is sold on either. The thank-you page runs a 2m55s primer video, then teaches "
         "inbox deliverability out loud &mdash; &ldquo;star this email and move it to your primary "
         "inbox&rdquo; &mdash; then add-to-calendar, then an IG follow, then a YouTube video to "
         "watch beforehand. The confirmation page adds a 5-point class checklist: desktop not "
         "phone, block 90 minutes, take notes and post them tagging both handles, engage live "
         "(&ldquo;Attention = Retention&rdquo;), screenshot and share to your IG story."),
        ("The price is never said, anywhere",
         "Not on a page, not on a slide, not in 19,078 transcribed words. At 75:09 she names two "
         "costs, programme and inventory, then immediately blurs them into one capital number "
         "and hands it to the call. The whole value-reframe stack that follows &mdash; a luxury "
         "vacation, a Chanel bag, college tuition &mdash; anchors against spending she assumes "
         "the avatar already does, without ever naming her own number."),
        ("Show-rate commitment is a forced choice, in writing",
         "Before a time can be picked the application states <b>&ldquo;we DO NOT accept "
         "cancellations or reschedules&rdquo;</b> and then makes her choose between "
         "&ldquo;I will choose a time and date that best fits my calendar and promise to show up "
         "on time&rdquo; and &ldquo;No I will not show up to my call on time&rdquo;. There is no "
         "neutral option."),
        ("The class is the top of their DM funnel",
         "At 85:17, an hour and 25 minutes in, she tells everyone still watching to DM the word "
         "<b>resource</b> on Instagram for a free guide. Attendance converts into inbound DM "
         "volume a human team can work. The lead magnet is deliberately withheld until deep into "
         "the runtime, so it doubles as a stay-to-the-end incentive."),
        ("The application disqualifies out loud",
         "Typeform Df2qD9dy has 14 jump rules and two terminal screens, one literally titled "
         "<b>&ldquo;DQ Leads&rdquo;</b> and one <b>&ldquo;Qualified lead&rdquo;</b>. Under 18, "
         "unwilling to commit 3 months, or unable to fund all route to the dead end."),
        ("The funnel is visibly half-maintained",
         "The WebinarJam registration resolves to w1505 and then bounces to "
         "1percentacademy.com/free-webi, a page that no longer exists and redirects to "
         "clickfunnels.com. Variant B's countdown reads 00:00:00. The replay page asserts a "
         "72-hour expiry over a timer that is also 00:00:00. The thank-you page still says "
         "Copyright 2025 while the opt-in says 2026."),
    ],

    "FUNNEL": [
        ("Opt-in &mdash; IG link in bio", "1percentacademy.com/optin-6405118817853424&hellip;",
         "The page Will was sent. &ldquo;Discover How Ambitious Girls Are Buying Back Their Time "
         "by Creating Premium Brands on Amazon.&rdquo; Evergreen countdown, &ldquo;Trusted By "
         "Over 2,347 Women&rdquo;, 150 spots."),
        ("Opt-in &mdash; variant B", "1percentacademy.com/optin",
         "Income + mechanism instead of identity: &ldquo;How Boss Women Are Building $10K/Mo "
         "Amazon FBA Businesses As Complete Beginners Using the Premium Brand Method.&rdquo; "
         "Darker buttons, dead countdown."),
        ("Opt-in &mdash; root and /masterclass", "1percentacademy.com/",
         "Two further live variants. /masterclass is byte-identical to the IG page."),
        ("Thank-you page", "1percentacademy.com/thank-you",
         "Primer video, inbox training, calendar add, IG follow, YouTube pre-work."),
        ("Confirmation page", "1percentacademy.com/confirmation",
         "The 5-point class checklist and the private live-room link "
         "(event.webinarjam.com/go/live/105/&hellip;). Follows both "
         "@jacquelinevagar and @sal_habibi."),
        ("The class", "WebinarJam",
         '<span class="tag bad">pre-recorded</span> 1h42m49s Wistia file, advertised as '
         "&ldquo;FREE LIVE MASTERCLASS: THURSDAY @ 2PM EST&rdquo;"),
        ("Replay page", "1percentacademy.com/replay",
         "&ldquo;This Replay Expires In 72 Hours&rdquo; over a 00:00:00 timer. Full webinar, "
         "then the application."),
        ("Application", "1percentacademy.com/application",
         "Typeform Df2qD9dy. Fomo social-proof widget fires over the top. Never submitted."),
    ],

    "TRANSCRIPT_GROUPS": [
        ("Masterclass &mdash; 1h 42m", [os.path.join(PKG, "Transcript/transcript_webinar.md")]),
        ("Registration-page VSL &mdash; 2m 55s",
         [os.path.join(PKG, "Transcript/transcript_registration_vsl.md")]),
    ],

    "SLIDE_PAGES": [
        ("Webinar slides", "webinar.html", "Screenshots", "web_",
         "174 slides from the 1h42m masterclass, presenter-only frames stripped. "
         "Bonus stack from 73:39, the money non-answer at 75:09, the visualisation close "
         "at 80:00, the DM-the-word-resource ask at 85:17."),
    ],

    "DECKS": [
        ("Masterclass &mdash; the full 1h42m pitch", 174,
         "https://docs.google.com/presentation/d/1nzfDCE0oOdHGh3BR5Eb0yVtyKvBSuyC697CbC2hpQzE/edit"),
    ],

    "VIDEOS": [
        ("webinar_replay_1080p.mp4", 6169, "483 MB",
         "The evergreen &ldquo;live&rdquo; masterclass. The entire pitch."),
        ("registration_vsl_1080p.mp4", 176, "65 MB",
         "The 2m55s primer that plays on the thank-you page. Pure show-up copy."),
    ],

    "ANALYSIS": """
<div class="note warn"><b>Read this first.</b> The masterclass advertised as
&ldquo;FREE LIVE &middot; THURSDAY @ 2PM EST&rdquo; is a recorded 1h42m49s file served from
Wistia. The scarcity around it &mdash; 150 spots, &ldquo;first 20 women&rdquo;, the 72-hour
replay expiry &mdash; is a production choice, not a constraint.</div>

<h2 class="sec">Why this one matters to us</h2>
<p>Different vertical, same machine. Female avatar with no experience, a
buy-back-your-time promise, a named mechanism, a free class, and a phone call at the end.
The two mechanics below are the reason it is in the file &mdash; both attack problems we
actually have, and neither depends on selling Amazon FBA.</p>

<h2 class="sec">The structure</h2>
<div class="tablewrap"><table>
<tr><th>Time</th><th>Beat</th><th>What she is doing</th></tr>
<tr><td>00:35</td><td>Promise</td><td>&ldquo;How to actually make $10,000 a month as a complete beginner in 2026&rdquo;</td></tr>
<tr><td>14:19</td><td>Objection sweep</td><td>Cost versus other businesses, then competition, then tariffs &mdash; pre-empted before teaching</td></tr>
<tr><td>23:56</td><td>Capital expectation</td><td>&ldquo;$3,000 to $5,000 to launch your first product the right way&rdquo; &mdash; the number that later gets blended with the programme fee</td></tr>
<tr><td>31:24</td><td>Girl math</td><td>A single worked P&amp;L: $35 product, 20 units/day, $8,400 monthly profit</td></tr>
<tr><td>33:41</td><td>Lifestyle translation</td><td>Each profit tier converted into an object &mdash; Louboutins, the Maldives, a Chanel bag, a G Wagon</td></tr>
<tr><td>48:00</td><td>Contrast</td><td>The average American salary against her one-week screenshots</td></tr>
<tr><td>61:20</td><td>Proof roll</td><td>Named members, each with a number and a timeframe</td></tr>
<tr><td>73:39</td><td>Stack</td><td>Accountability coach, 100 products, DFY listing, live calls, lifetime course</td></tr>
<tr><td><b>75:09</b></td><td><b>The money non-answer</b></td><td>Names two costs, blurs them, hands the number to the call</td></tr>
<tr><td>76:03</td><td>Reframe stack</td><td>Vacation, handbag, tuition &mdash; all spending she assumes the avatar already does</td></tr>
<tr><td>78:54</td><td>Scarcity bonus</td><td>First 20 women get the software free, framed at $1,100</td></tr>
<tr><td>79:37</td><td>Scam objection</td><td>Names it out loud, then goes straight into the close</td></tr>
<tr><td>80:00</td><td>Visualisation</td><td>A three-minute guided eyes-closed exercise ending in &ldquo;would she invest in herself?&rdquo;</td></tr>
<tr><td>83:21</td><td>FAQ</td><td>Country eligibility, hours per day, time to launch, what if it fails, logistics</td></tr>
<tr><td>85:17</td><td>DM ask</td><td>&ldquo;DM me the word <b>resource</b> on Instagram&rdquo;</td></tr>
<tr><td>86:05</td><td>Member interviews</td><td>Two recorded member calls play out to the end</td></tr>
</table></div>

<h2 class="sec">Worth taking</h2>
<div class="grid g2">
<div class="card"><h3>Qualify for money at registration, not at application</h3>
<p>One required dropdown on the opt-in, two bands, posted to their own endpoint before the
webinar platform sees the lead. Every registrant carries a capital tag from minute zero, which
means the follow-up, the setter queue and the ad optimisation can all be sorted by it. We
currently learn budget far later, and only for the people who make it to a call.</p></div>
<div class="card"><h3>Spend two pages on attendance</h3>
<p>Nothing is sold on the thank-you or confirmation pages. They teach inbox deliverability by
name, demand desktop over phone, ask for a 90-minute block, and convert the registrant into a
public commitment via an IG story. Show rate is our number-one bottleneck and this is the
cheapest version of attacking it we have seen.</p></div>
<div class="card"><h3>Make the show-up promise a forced choice</h3>
<p>&ldquo;We DO NOT accept cancellations or reschedules&rdquo;, then two options with no neutral
middle. Whether or not they enforce it, the lead has typed the commitment before she gets a
slot.</p></div>
<div class="card"><h3>Withhold the lead magnet until 85 minutes in</h3>
<p>The free guide is only announced near the end and only via an Instagram DM. It buys retention
to the close and pours warm inbound into a channel a human can work.</p></div>
<div class="card"><h3>Translate profit into objects, not percentages</h3>
<p>$280/day becomes a pair of Louboutins; $8,400/month becomes a Chanel bag. The arithmetic is
ordinary; the translation is what makes it land for this avatar.</p></div>
<div class="card"><h3>Name the scam objection yourself</h3>
<p>&ldquo;I don't know if this is a scam &hellip; I've been burned in the past&rdquo; &mdash; said
in her own voice, immediately before the close, rather than left for the setter.</p></div>
</div>

<h2 class="sec">Not worth taking</h2>
<p>The fake-live framing and the dead timers. The replay page asserts a 72-hour expiry over a
counter reading 00:00:00, and the WebinarJam registration path dead-ends on a page that no
longer exists. Anyone who checks can see it, and the whole funnel is built for an avatar who is
already scanning for reasons to distrust &mdash; she says so herself at 79:37.</p>
<p>The blended price is a genuine trade-off rather than a clean win. Refusing to name a number
protects the call, but it also means every booked call spends its first minutes doing price
discovery, and the application's own budget bands (&lt;$5k through $15k+) leak the range anyway.</p>

<h2 class="sec">Open questions</h2>
<ul class="ul">
<li>What the Zapier hook does with the budget answer &mdash; route, prioritise, or exclude &mdash;
is not observable from outside.</li>
<li>The registration form did not render on any live variant we captured, so we cannot tell
whether the money gate is currently running or is leftover markup.</li>
<li>No email sequence has been captured yet. The research identity has not opted in, because the
form requires a phone number and we do not have a research number.</li>
<li>@sal_habibi appears alongside @jacquelinevagar on the confirmation page. Second operator,
probably the one running traffic, not yet investigated.</li>
</ul>
""",
}

if __name__ == "__main__":
    build(CONFIG)
