# Behavioral: Handling a Tight Deadline

## Question
"Describe a time you were forced to work under a tight deadline. How did you handle the pressure, and what was the outcome?"

## STAR Template

### Situation
(Describe the project, why the deadline was tight, and your role.)

### Task
(What specifically needed to be finished by the deadline?)

### Action
(What steps did you take? Did you prioritize certain tasks? Delegate? Communicate with stakeholders?)

### Result
(Did you meet the deadline? What was the final outcome/impact?)

## Key Focus Areas
- **Communication:** Proactive updates to stakeholders.
- **Prioritization:** Identifying "must-haves" vs "nice-to-haves".
- **Composure:** Maintaining quality under pressure.

I was in charge of creating a statistics pipeline for ROSSA that would run descriptive and inferential statistics on changes to a users' study. My goal was to finish the statistics pipeline before the next group grant meeting. I had to build a system that would ensure the stats were never stale and ran on the correct information across multiple modalities, sample groups, and comparison groups, without the need for user intervention. When the user navigates to the report at the end of the study, the stats should be there ready for them. I built a system of observers that would watch for changes in the sample groups, comparison groups and uploads, and run stats where either data was ready, or old data was modified. For example, if a user were to upload a comparison group, which is a comparison of sample groups, I would gather the uploads tied to each sample group within the study, and run inferential stats jobs for each modality or context paired with the comparison group. Since I was working on orchestrating it, and we were undecided on the python implementation, I had another dev helping me on some integrations of specific stats computations, informing him what information his function would receive and what structure the output should take to ensure consistency across the stats pipeline. Provided this was a massive undertaking, I had to understand we would not have a frontend implementation to show the client, much less, have all of the stats completed. I communicated with the client, and he of course was understanding, and my final outcome before the meeting was finishing the overall stats orchestration and demonstrating a table of descriptive statistics that ran locally. Eventually, the system was finished and has since been iterated upon to improve coverage - expanded context has been added for additional modalities, optimized jobs using versioning and modality based keys to prevent redundant stats runs and ensure that styats run on current data.
