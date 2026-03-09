# Reference: Behavioral STAR Method (Tier 1 Behavioral)
# Topic: Conflict Resolution

## Questions:
1. "Describe a time you had a technical disagreement with a colleague. How did you approach the conversation, and what was the outcome?" (Use STAR Method)
2. In your response, emphasize how you balanced your engineering judgment with the team's shared goals.

# TODO (Answer in Markdown)
1. possible answers:
 - determining how to run the stats - in php or python. We had to run descriptive stats and inferential stats. Descriptive deals with one type of sample, and inferential compares different types of samples. Native php does not have much math or statistics support, and neither does the mathPHP library. From original discussion, the full timer was convinced we would just write it in php since it was just math, but I thought since there was stronger support in python, we should use that. He wanted to lower complexity, but I argued that it would increase complexity having to fill in gaps of missing stats functions from mathphp with our own implementations. We eventually got to a point where we were using php for supported functions and python for functions that scipy would handle. However, this was also not optimal since we were starting a process for each calculation (per measurement per comparison group per funtion) - incredible fanout. Instead we batched by the comparison groups and passed all measurement information over so that the inferential stats would only start one process per comparison group, and return all values per measurement and function. Descriptive stats remained in php as they were lighter and had native support. Our initial solution was to modularize statistics and organize the statistic workflow so that the functions could readily be replaced (however, this lead to the fanout of python processes, so we had to decide to fully switch to python for the inferential stats) - outcome was attempted implementation of just php that forced us into a decision to use python, and then further optimize to use MORE python

 - end result was running the inferential stats fully in python in one batch process instead of spawning a process for each type of inferential stat that was not available in mathphp.

 other options? even disagreements with clients?
 - disagreeing over the roles/permission based architecture with coworker (early decision) - ended on a compromise of roles/permission combination, were permissions are assigned to roles and also independently to users. discussion was about which would be easiest to implement and also adjust. I think that coworker was advocating for permissions and I said roles, and we ended up combining them through conversation? this was a long time ago
 - suggest adding steps to the upload process (get implemented later) INCLUDING a completed status - improves the statistics workflow because otherwise the status is computed and not always accurate
 - determing how to display the instructions for comparison group builder (i wanted to put in a form that would pop up on page open, client wanted it at top of page, but the instructions are large and bloat the page)
 - determining the upload process and where to run stats. I was advocating for finalize step because stats jobs were triggered for incomplete uploads too often.
 - determing how to show the group statistics table - determing how to structure the group statistics and whether researchers would be more concerned on data per sample group or the comparison groups made by the study. determining how to filter by comparison group and/or context/modality. Which one should go at the higher level? email to client cleared it up
 - talking about it being too late to add coverage to application and that it would require a refactor for more modularity