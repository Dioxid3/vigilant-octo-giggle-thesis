#%%
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd # tool to prepare and analyze data
import matplotlib.pyplot as plt # tool to visualize data
import seaborn as sns # tool to visualize data
import pingouin as pg # tool for complex analysis and tests
import numpy as np
from scipy.stats import spearmanr

# Creating a dataframe from the questionnaire csv
# Try clause as different kernels are being annoying about the path and I can't be bothered to fix it
try:
    df = pd.read_csv('questionnaire.csv', sep=';', decimal=',')
except:
    df = pd.read_csv('vigilant-octo-giggle-thesis\questionnaire.csv', sep=';', decimal=',')


colors = sns.color_palette("hls", 7)
#print(df.to_string())


#%%
#########################
# Demographic Variables #
#########################

age_group = df['Age Group']
age_group_counts = df['Age Group'].value_counts()
age_group_counts.reindex(range(1,8),fill_value=0)
age_group_counts[5] = 0
age_group_counts[6] = 0
age_group_counts[7] = 0
age_group_counts = age_group_counts.sort_index()
age_group_counts = age_group_counts.rename({1: '≤ 25', 2: '26-35', 3: '36-45', 4: '46-55', 5: '56-65', 6: '≥ 65', 7:'Prefer not to answer'})
age_group_total_responses = age_group_counts.sum()
age_group_percentages = (age_group_counts / age_group_total_responses) * 100

ax = age_group_counts.plot(kind='barh')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.title('Distribution of Age Groups')
for i, v in enumerate(age_group_counts):
    if v > 10:  # Place inside the bar if value is greater than 10
        ax.text(v - 0.5, i, f'{v} ({age_group_percentages[i]:.2f}%)', color='black', va='center', ha='right')
    else:  # Place outside the bar if value is small or zero
        ax.text(v + 0.5, i, f'{v} ({age_group_percentages[i]:.2f}%)', color='black', va='center', ha='left')

#%%
work_years = df['Work years (Current career)']
work_years_counts = df['Work years (Current career)'].value_counts()
work_years_counts.reindex(range(1,7),fill_value=0)
work_years_counts[6] = 0
work_years_counts = work_years_counts.sort_index()
work_years_counts = work_years_counts.rename({1: '≤ 5', 2: '6-10', 3: '11-15', 4: '16-20', 5: '≥ 20', 6:'Prefer not to answer'})
work_years_total_responses = work_years_counts.sum()
work_years_percentages = (work_years_counts / work_years_total_responses) * 100

ax = work_years_counts.plot(kind='barh')
plt.xlabel('Work years (Current career)')
plt.ylabel('Count')
plt.title('Distribution of Work years (Current career)s')
for i, v in enumerate(work_years_counts):
    if v > 10:  # Place inside the bar if value is greater than 10
        ax.text(v - 0.5, i, f'{v} ({work_years_percentages[i]:.2f}%)', color='black', va='center', ha='right')
    else:  # Place outside the bar if value is small or zero
        ax.text(v + 0.5, i, f'{v} ({work_years_percentages[i]:.2f}%)', color='black', va='center', ha='left')


#%%
line_of_work = df['Line of work Select closest that applies']
line_of_work_counts = df['Line of work Select closest that applies'].value_counts()
line_of_work_counts.reindex(range(1,9),fill_value=0)
line_of_work_counts[6] = 0
line_of_work_counts = line_of_work_counts.sort_index()
line_of_work_counts = line_of_work_counts.rename({1: 'Software Development', 2: 'Management', 3: 'Administrative', 4: 'Consulting', 5: 'Support', 6: 'Design', 7:'Sales & Marketing', 8:'Prefer not to answer'})
line_of_work_total_responses = line_of_work_counts.sum()
line_of_work_percentages = (line_of_work_counts / line_of_work_total_responses) * 100

ax = line_of_work_counts.plot(kind='barh')
plt.xlabel('Line of work Select closest that applies')
plt.ylabel('Count')
plt.title('Distribution of Line of work Select closest that applies')
for i, v in enumerate(line_of_work_counts):
    if v > 10:  # Place inside the bar if value is greater than 10
        ax.text(v - 0.5, i, f'{v} ({line_of_work_percentages[i]:.2f}%)', color='black', va='center', ha='right')
    else:  # Place outside the bar if value is small or zero
        ax.text(v + 0.5, i, f'{v} ({line_of_work_percentages[i]:.2f}%)', color='black', va='center', ha='left')


#%%
working_hours = df['Working hours']
working_hours_counts = df['Working hours'].value_counts()
working_hours_counts.reindex(range(1,4),fill_value=0)
working_hours_counts[3] = 0
working_hours_counts = working_hours_counts.sort_index()
working_hours_counts = working_hours_counts.rename({1: 'Full-time', 2: 'Part-time', 3: 'Prefer not to answer'})
working_hours_total_responses = working_hours_counts.sum()
working_hours_percentages = (working_hours_counts / working_hours_total_responses) * 100

ax = working_hours_counts.plot(kind='barh')
plt.xlabel('Working hours')
plt.ylabel('Count')
plt.title('Distribution of Working hours')
for i, v in enumerate(working_hours_counts):
    if v > 10:  # Place inside the bar if value is greater than 10
        ax.text(v - 0.5, i, f'{v} ({working_hours_percentages[i]:.2f}%)', color='black', va='center', ha='right')
    else:  # Place outside the bar if value is small or zero
        ax.text(v + 0.5, i, f'{v} ({working_hours_percentages[i]:.2f}%)', color='black', va='center', ha='left')



#%%
office_visits = df['On average I visit office where I see my colleagues']
office_visits_counts = df['On average I visit office where I see my colleagues'].value_counts()
office_visits_counts.reindex(range(1,6),fill_value=0)
office_visits_counts[5] = 0
office_visits_counts = office_visits_counts.sort_index()
office_visits_counts = office_visits_counts.rename({1: 'Less than any other option', 2: '1-2 times a week', 3: '3-4 times a week', 4: 'Everyday', 5: 'Prefer not to answer'})
office_visits_total_responses = office_visits_counts.sum()
office_visits_percentages = (office_visits_counts / office_visits_total_responses) * 100


ax = office_visits_counts.plot(kind='barh')
plt.xlabel('On average I visit office where I see my colleagues')
plt.ylabel('Count')
plt.title('Distribution of \'On average I visit office where I see my colleagues\'')
for i, v in enumerate(office_visits_counts):
    if v > 10:  # Place inside the bar if value is greater than 10
        ax.text(v - 0.5, i, f'{v} ({office_visits_percentages[i]:.2f}%)', color='black', va='center', ha='right')
    else:  # Place outside the bar if value is small or zero
        ax.text(v + 0.5, i, f'{v} ({office_visits_percentages[i]:.2f}%)', color='black', va='center', ha='left')


#%%
team_size = df['My team consists of']
team_size_counts = df['My team consists of'].value_counts()
team_size_counts.reindex(range(1,6),fill_value=0)
team_size_counts = team_size_counts.sort_index()
team_size_counts = team_size_counts.rename({1: 'Less than 3 people', 2: '3-5 people', 3: '5-10 people', 4: 'More than 10 people', 5: 'Prefer not to answer'})
team_size_total_responses = team_size_counts.sum()
team_size_percentages = (team_size_counts / team_size_total_responses) * 100

ax = team_size_counts.plot(kind='barh')
plt.xlabel('My team consists of')
plt.ylabel('Count')
plt.title('Distribution of My team consists of')
for i, v in enumerate(team_size_counts):
    if v > 10:  # Place inside the bar if value is greater than 10
        ax.text(v - 0.5, i, f'{v} ({team_size_percentages[i]:.2f}%)', color='black', va='center', ha='right')
    else:  # Place outside the bar if value is small or zero
        ax.text(v + 0.5, i, f'{v} ({team_size_percentages[i]:.2f}%)', color='black', va='center', ha='left')



#%%
#########################
#  Employee Engagement  #
#########################

vigor = df[['vigor1','vigor2','vigor3','vigor4','vigor5', 'vigor6']]
#print(vigor.to_string)
dedication = df[['dedication1','dedication2','dedication3','dedication4','dedication5']]
#print(dedication.to_string)
absorption = df[['absorption1','absorption2','absorption3','absorption4','absorption5','absorption6']]
#print(absorption.to_string)

# Testing the reliability of each group depicting Vigor Absorption and Dedication 
print("Cronbach's Alpha for Vigor, with 95%% confidence interval" + str(pg.cronbach_alpha(data=vigor)))
print("Cronbach's Alpha for Dedication, with 95%% confidence interval" + str(pg.cronbach_alpha(data=dedication)))
print("Cronbach's Alpha for Absorption, with 95%% confidence interval" + str(pg.cronbach_alpha(data=absorption)))
print("\n"*2) # Creates spacing between prints

#%%
## Boxplots
# Plotting Likert scale responses for each item
# Vigor
plt.figure(figsize=(10, 6))
sns.boxplot(data=vigor)
plt.xlabel('Likert Scale Item')
plt.ylabel('Response')
plt.title('Distribution of Likert Scale Responses - Vigor')
plt.subplots_adjust(bottom=0.30)

# Wrap x-axis labels
plt.xticks(rotation=45, ha='right')
plt.gca().xaxis.set_tick_params(labelsize=8)  # Adjust label size if needed

for tick in plt.gca().xaxis.get_major_ticks():
    tick.label1.set_wrap(True)
    tick.label1.set_rotation(45)


# Dedication
plt.figure(figsize=(10, 6))
sns.boxplot(data=dedication)
plt.xlabel('Likert Scale Item')
plt.ylabel('Response')
plt.title('Distribution of Likert Scale Responses - Dedication')
plt.subplots_adjust(bottom=0.30)

# Wrap x-axis labels
plt.xticks(rotation=45, ha='right')
plt.gca().xaxis.set_tick_params(labelsize=8)  # Adjust label size if needed
for tick in plt.gca().xaxis.get_major_ticks():
    tick.label1.set_wrap(True)
    tick.label1.set_rotation(45)


# Absorption
plt.figure(figsize=(10, 6))
sns.boxplot(data=absorption)
plt.xlabel('Likert Scale Item')
plt.ylabel('Response')
plt.title('Distribution of Likert Scale Responses - Absorption')
plt.subplots_adjust(bottom=0.30)

# Wrap x-axis labels
plt.xticks(rotation=45, ha='right')
plt.gca().xaxis.set_tick_params(labelsize=8)  # Adjust label size if needed
for tick in plt.gca().xaxis.get_major_ticks():
    tick.label1.set_wrap(True)
    tick.label1.set_rotation(45)


#%%
## Sum variables
# Creating sum variables by summing the columns of each group together and diving by the number of columns
vigor_sum = vigor.sum(axis=1)/len(vigor.columns)
dedication_sum = dedication.sum(axis=1)/len(dedication.columns)
absorption_sum = absorption.sum(axis=1)/len(absorption.columns)

print(vigor_sum.head())
print(dedication_sum.head())
print(absorption_sum.head())

# Plotting Likert scale responses for the sum items
engagement_sum = pd.DataFrame({'Vigor': vigor_sum, 'Dedication': dedication_sum, 'Absorption': absorption_sum})
engagement_sum_data_melted = engagement_sum.melt(var_name='Factor', value_name='Response Sum')

plt.figure(figsize=(10, 6))
sns.boxplot(x='Factor', y='Response Sum', data=engagement_sum_data_melted)
plt.title('Engagement Sum Variables - Sum Box Plot')
plt.xlabel('Factor')
plt.ylabel('Sum')

# Wrap x-axis labels
plt.xticks(rotation=0, ha='center')
plt.gca().xaxis.set_tick_params(labelsize=8)  # Adjust label size if needed
for tick in plt.gca().xaxis.get_major_ticks():
    tick.label1.set_wrap(True)
    tick.label1.set_rotation(0)


#%%
#########################
# Communication mediums #
#########################

# Reliability of communication mediums
communication_mediums = df[['CM_multiple','CM_unreliability','CM_functionalities', 'CM_information','CM_jumping','CM_notifications']]
#print(communication_mediums.head())

# Calculate Cronbach's alpha for the group
communication_mediums_alpha_group = pg.cronbach_alpha(communication_mediums)

# Create a DataFrame to store Cronbach's alpha for each item removal
alpha_item_removal = pd.DataFrame(columns=['Item', 'Alpha'])

# Iterate over each item and calculate alpha when the item is removed
for column in communication_mediums.columns:
    communication_mediums_temp = communication_mediums.drop(column, axis=1)
    alpha_temp = pg.cronbach_alpha(communication_mediums_temp)
    alpha_item_removal = pd.concat([alpha_item_removal, pd.DataFrame({'Item': [column], 'Alpha': [alpha_temp]})], ignore_index=True)

# Sort the DataFrame by alpha value
alpha_item_removal = alpha_item_removal.sort_values(by='Alpha', ascending=False)
print(alpha_item_removal)

#%%
## Detractors
communication_mediums_detractors = communication_mediums[['CM_multiple','CM_jumping','CM_notifications']]
print("Cronbach's Alpha for Communication Mediums\' detracting qualities, with 95%% confidence interval" + str(pg.cronbach_alpha(data=communication_mediums_detractors)))

#%% Reliability of communication mediums' detractors

# Calculate Cronbach's alpha for the group
communication_mediums_alpha_group = pg.cronbach_alpha(communication_mediums_detractors)

# Create a DataFrame to store Cronbach's alpha for each item removal
alpha_item_removal = pd.DataFrame(columns=['Item', 'Alpha'])

# Iterate over each item and calculate alpha when the item is removed
for column in communication_mediums_detractors.columns:
    communication_mediums__detractors_temp = communication_mediums_detractors.drop(column, axis=1)
    alpha_temp = pg.cronbach_alpha(communication_mediums__detractors_temp)
    alpha_item_removal = pd.concat([alpha_item_removal, pd.DataFrame({'Item': [column], 'Alpha': [alpha_temp]})], ignore_index=True)

# Sort the DataFrame by alpha value
alpha_item_removal = alpha_item_removal.sort_values(by='Alpha', ascending=False)
print(alpha_item_removal)

# Removing the last bad fit
# communication_mediums_detractors = communication_mediums_detractors.drop(columns=['CM_unreliability'], inplace=True)
print("Cronbach's Alpha for Communication Mediums\' detracting qualities, with 95%% confidence interval" + str(pg.cronbach_alpha(data=communication_mediums_detractors)))


#%%
## Communication mediums, other
# Other
communication_mediums_other = communication_mediums[['CM_unreliability','CM_functionalities', 'CM_information']]
print("Cronbach's Alpha for Communication Mediums' other qualities, with 95%% confidence interval" + str(pg.cronbach_alpha(data=communication_mediums_other)))


#%%
# Plotting Likert scale responses for each item
plt.figure(figsize=(10, 6))
sns.boxplot(data=communication_mediums_detractors)
plt.xlabel('Likert Scale Item')
plt.ylabel('Response')
plt.title('Distribution of Likert Scale Responses - Communication Mediums\' detracting qualities')
plt.subplots_adjust(bottom=0.30)

# Wrap x-axis labels
plt.xticks(rotation=45, ha='right')
plt.gca().xaxis.set_tick_params(labelsize=8)  # Adjust label size if needed

for tick in plt.gca().xaxis.get_major_ticks():
    tick.label1.set_wrap(True)
    tick.label1.set_rotation(45)

plt.figure(figsize=(10, 6))
sns.boxplot(data=communication_mediums_other)
plt.xlabel('Likert Scale Item')
plt.ylabel('Response')
plt.title('Distribution of Likert Scale Responses - Communication Mediums\' other qualities')
plt.subplots_adjust(bottom=0.30)


plt.figure(figsize=(10, 6))
sns.boxplot(data=communication_mediums)
plt.xlabel('Likert Scale Item')
plt.ylabel('Response')
plt.title('Distribution of Likert Scale Responses - Communication Mediums')
plt.subplots_adjust(bottom=0.30)


# Wrap x-axis labels
plt.xticks(rotation=45, ha='right')
plt.gca().xaxis.set_tick_params(labelsize=8)  # Adjust label size if needed

for tick in plt.gca().xaxis.get_major_ticks():
    tick.label1.set_wrap(True)
    tick.label1.set_rotation(45)


#%%

#########################
#     Social needs      #
#########################


social_needs = df[['SN_news','SN_nonworktopics','SN_worktopics','SN_onlineequalsf2f','SN_onlinenonverbal','SN_remotelonely','SN_multitask','SN_f2fvsdigital']]
#print(social_needs.head())

plt.figure(figsize=(10, 6))
sns.boxplot(data=social_needs)
plt.title('Social Needs Variables')
plt.xlabel('Response')
plt.ylabel('Factor')

# Calculate Cronbach's alpha for the group
social_needs_alpha_group = pg.cronbach_alpha(social_needs)

# Create a DataFrame to store Cronbach's alpha for each item removal
alpha_item_removal = pd.DataFrame(columns=['Item', 'Alpha'])

# Iterate over each item and calculate alpha when the item is removed
for column in social_needs.columns:
    social_needs_temp = social_needs.drop(column, axis=1)
    alpha_temp = pg.cronbach_alpha(social_needs_temp)
    alpha_item_removal = pd.concat([alpha_item_removal, pd.DataFrame({'Item': [column], 'Alpha': [alpha_temp]})], ignore_index=True)

# Sort the DataFrame by alpha value
alpha_item_removal = alpha_item_removal.sort_values(by='Alpha', ascending=False)
print(alpha_item_removal)

#%%
# Satisfaction remote vs on-site
social_needs_satisfaction_remote_vs_onsite = df[['SN_onlineequalsf2f','SN_onlinenonverbal']]
print("Cronbach's Alpha for satisfaction of remote versus on-site communication, with 95%% confidence interval" + str(pg.cronbach_alpha(data=social_needs_satisfaction_remote_vs_onsite)))
social_needs_satisfaction_remote_vs_onsite_sum = social_needs_satisfaction_remote_vs_onsite.sum(axis=1)/len(social_needs_satisfaction_remote_vs_onsite.columns)

# Loneliness
social_needs_loneliness = df[['SN_remotelonely','SN_f2fvsdigital']]
print("Cronbach's Alpha for feelings of loneliness, with 95%% confidence interval" + str(pg.cronbach_alpha(data=social_needs_loneliness)))
social_needs_loneliness_sum = social_needs_loneliness.sum(axis=1)/len(social_needs_loneliness.columns)

# Discussion topics
social_needs_discussion_topics = df[['SN_nonworktopics','SN_worktopics']]
print("Cronbach's Alpha for importance of different discussion topics, with 95%% confidence interval" + str(pg.cronbach_alpha(data=social_needs_discussion_topics)))
social_needs_discussion_topics_sum = social_needs_discussion_topics.sum(axis=1)/len(social_needs_discussion_topics.columns)

# News satisfaction
social_needs_news_satisfaction = df[['SN_news']]
#print(social_needs_news_satisfaction.head())



""" print(social_needs_satisfaction_remote_vs_onsite_sum.head())
print(social_needs_loneliness_sum.head())
print(social_needs_discussion_topics_sum.head())"""

#%%
# Plotting Likert scale responses for the sum items
social_needs_sum = pd.DataFrame({'Satisfaction remote vs on-site': social_needs_satisfaction_remote_vs_onsite_sum, 'Loneliness': social_needs_loneliness_sum, 'Discussion topics': social_needs_discussion_topics_sum})
social_needs_sum_data_melted = social_needs_sum.melt(var_name='Factor', value_name='Response Sum')

plt.figure(figsize=(10, 6))
sns.boxplot(x='Factor', y='Response Sum', data=social_needs_sum_data_melted)
plt.title('Social Needs Sum Variables - Sum Box Plot')
plt.xlabel('Factor')
plt.ylabel('Sum')

# Wrap x-axis labels
plt.xticks(rotation=0, ha='center')
plt.gca().xaxis.set_tick_params(labelsize=8)  # Adjust label size if needed
for tick in plt.gca().xaxis.get_major_ticks():
    tick.label1.set_wrap(True)
    tick.label1.set_rotation(0)


#%%
social_needs_concat = pd.concat([social_needs_sum, social_needs_news_satisfaction], ignore_index=True)
social_needs_concat_melted = social_needs_concat.melt(var_name='Factor', value_name='Response')

# Create a box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Factor', y='Response', data=social_needs_concat_melted)
plt.title('Social Needs Variables - Box Plot')
plt.xlabel('Factor')
plt.ylabel('Response')

# Wrap x-axis labels
plt.xticks(rotation=0, ha='center')
plt.gca().xaxis.set_tick_params(labelsize=8)  # Adjust label size if needed
for tick in plt.gca().xaxis.get_major_ticks():
    tick.label1.set_wrap(True)
    tick.label1.set_rotation(0)


#%% 
daily_tools = df[['Company Wiki','Email','Slack','Microsoft Teams','Jira','Productboard','SE_CM']]

# Calculate the total number of respondents
daily_tools_total_respondents = len(daily_tools)

# Calculate the usage counts for each tool
daily_tools_usage_counts = daily_tools.sum()

# Calculate the percentage of usage for each tool
daily_tools_usage_percentages = (daily_tools_usage_counts / daily_tools_total_respondents) * 100

# Create a bar plot
plt.figure(figsize=(10, 6))
ax = daily_tools_usage_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Tools')
plt.ylabel('Count')
plt.title('Tools Used in Daily Work')
plt.grid(axis='y')  # Add grid lines to the y-axis for better readability
plt.yticks(range(0, 101, 10)) # set Y-axis ticks for every 10% instead of default 20%

for index, value in enumerate(daily_tools_usage_counts):
    percentage = daily_tools_usage_percentages[index]
    ax.text(index, value - 0.2, f'n={value}\n{percentage:.1f}%', ha='center', va='top', color='black', fontsize=10)


# Wrap x-axis labels
plt.xticks(rotation=0, ha='center')
plt.gca().xaxis.set_tick_params(labelsize=8)  # Adjust label size if needed
for tick in plt.gca().xaxis.get_major_ticks():
    tick.label1.set_wrap(True)
    tick.label1.set_rotation(0)


#%% Stacked bar plot important customization
important_customizations = df[['Themes','Emojis','Gifs','Automation of Workflows','Integrations to other applications','Amount of channels/chats']]

# Define the Likert categories & mappings
likert_categories = ['Strongly Disagree', 'Disagree', 'Somewhat Disagree', 'Neutral', 'Somewhat Agree', 'Agree', 'Strongly Agree']
likert_mappings = {1: 'Strongly Disagree', 2: 'Disagree', 3: 'Somewhat Disagree', 4: 'Neutral', 5: 'Somewhat Agree', 6: 'Agree', 7: 'Strongly Agree'}

# Replace integer values with Likert categories
likert_data = important_customizations.replace(likert_mappings)

# Count the frequency of each response category for each item
likert_counts = likert_data.apply(pd.Series.value_counts)

# Reindex the DataFrame to include all Likert categories (filling NaN values with 0, although there shouldn't be any),
# and transpose for plotting
likert_counts = likert_counts.reindex(likert_categories, fill_value=0)
likert_counts_transposed = likert_counts.T

# Calculate the percentage of answers for each Likert category, transpose for plotting
likert_percentages = (likert_counts / likert_counts.sum()) * 100
likert_percentages_transposed = likert_percentages.T

#%%
# Create a horizontal stacked bar plot with adjusted plot settings
plt.figure(figsize=(12, 8))
likert_counts_transposed.plot(kind='barh', stacked=True, color=colors)
plt.ylabel('Items')
plt.xlabel('Frequency')
plt.title('Horizontal Stacked Bar Plot of Likert-Type Items')
plt.legend(title='Likert Scale', loc='lower left', bbox_to_anchor=(1, 1))

for n in likert_percentages_transposed:
    for i, (cs, ab, pc) in enumerate(zip(likert_percentages_transposed.iloc[:, :].cumsum(1)[n],  
                                         likert_percentages_transposed[n], likert_percentages_transposed[n])):
        if pc >= 7:
            plt.text(cs - ab / 2, i, f'{pc:.1f}%', va='center', ha='center')

#%% Stacked bar plot for variables

# Define the Likert categories & mappings
likert_categories = ['Strongly Disagree', 'Disagree', 'Somewhat Disagree', 'Neutral', 'Somewhat Agree', 'Agree', 'Strongly Agree']
likert_mappings = {1: 'Strongly Disagree', 2: 'Disagree', 3: 'Somewhat Disagree', 4: 'Neutral', 5: 'Somewhat Agree', 6: 'Agree', 7: 'Strongly Agree'}

df_list = [vigor, absorption, dedication, communication_mediums,social_needs, important_customizations]
for data_frame in df_list:
    # Replace integer values with Likert categories
    likert_data = data_frame.replace(likert_mappings)

    # Count the frequency of each response category for each item
    likert_counts = likert_data.apply(pd.Series.value_counts)

    # Reindex the DataFrame to include all Likert categories (filling NaN values with 0, although there shouldn't be any),
    # and transpose for plotting
    likert_counts = likert_counts.reindex(likert_categories, fill_value=0)
    likert_counts_transposed = likert_counts.T

    # Calculate the percentage of answers for each Likert category, transpose for plotting
    likert_percentages = (likert_counts / likert_counts.sum()) * 100
    likert_percentages_transposed = likert_percentages.T


    # Create a horizontal stacked bar plot with adjusted plot settings
    plt.figure(figsize=(12, 8))
    likert_counts_transposed.plot(kind='barh', stacked=True, color=colors)
    plt.ylabel('Items')
    plt.xlabel('Frequency')
    plt.title('Horizontal Stacked Bar Plot of Likert-Type Items')
    plt.legend(title='Likert Scale', loc='best', bbox_to_anchor=(1, 1))

    for n in likert_percentages_transposed:
        for i, (cs, ab, pc) in enumerate(zip(likert_percentages_transposed.iloc[:, :].cumsum(1)[n],  
                                            likert_percentages_transposed[n], likert_percentages_transposed[n])):
            if pc >= 7:
                plt.text(cs - ab / 2, i, f'{pc:.1f}%', va='center', ha='center')




#%%
engagement = (vigor_sum + absorption_sum + dedication_sum)/3


pg.multivariate_normality(engagement_sum)


engagement_communication_mediums_other_concat = pd.concat([engagement, communication_mediums_other], axis=1)
engagement_communication_mediums_detractors_concat = pd.concat([engagement, communication_mediums_detractors], axis=1)
##
engagement_demographics_concat = pd.concat([engagement, age_group, work_years, office_visits, working_hours, team_size], axis=1)
engagement_sum_demographics_concat = pd.concat([engagement_sum, age_group, work_years, office_visits, working_hours, team_size], axis=1)

engagement_sum_communication_mediums_concat = pd.concat([engagement_sum, communication_mediums], axis=1)
engagement_sum_communication_mediums_other_concat = pd.concat([engagement_sum, communication_mediums_other], axis=1)
engagement_sum_communication_mediums_detractors_concat = pd.concat([engagement_sum, communication_mediums_detractors], axis=1)

engagement_sum_social_needs_concat = pd.concat([engagement_sum, social_needs], axis=1)
engagement_sum_social_needs_sum_concat = pd.concat([engagement_sum, social_needs_sum, social_needs_news_satisfaction], axis=1)
engagement_sum_social_needs_loneliness_sum_concat = pd.concat([engagement_sum, social_needs_loneliness_sum], axis=1)
engagement_sum_social_needs_discussion_topics_sum_concat = pd.concat([engagement_sum, social_needs_discussion_topics_sum], axis=1)

communication_mediums_social_needs_concat = pd.concat([communication_mediums, social_needs], axis=1)
communication_mediums_detractors_social_needs_loneliness_sum_concat = pd.concat([communication_mediums_detractors, social_needs_loneliness_sum], axis=1)
communication_mediums_detractors_social_needs_discussion_topics_sum_concat = pd.concat([communication_mediums_detractors, social_needs_discussion_topics_sum], axis=1)

social_needs_important_customizations_concat = pd.concat([social_needs, important_customizations], axis=1)
communication_mediums_important_customizations_concat = pd.concat([communication_mediums, important_customizations], axis=1)

age_group_social_needs_sum_concat = pd.concat([age_group, office_visits, social_needs_sum], axis=1)


#%%
print(pg.multivariate_normality(engagement_sum_demographics_concat))
engagement_sum_demographics_concat.corr(method='spearman')
#%%
rho = engagement_sum_demographics_concat.corr(method='spearman')
pval = engagement_sum_demographics_concat.corr(method=lambda x, y: spearmanr(x, y)[1]) - np.eye(*rho.shape)
p = pval.applymap(lambda x: ''.join(['*' for t in [.05, .01, .001] if x<=t]))
rho.round(2).astype(str) + p

########
########

#%%
print(pg.multivariate_normality(engagement_sum_communication_mediums_concat))
engagement_sum_communication_mediums_concat.corr(method='spearman')

#%%
rho = engagement_sum_communication_mediums_concat.corr(method='spearman')
pval = engagement_sum_communication_mediums_concat.corr(method=lambda x, y: spearmanr(x, y)[1]) - np.eye(*rho.shape)
p = pval.applymap(lambda x: ''.join(['*' for t in [.05, .01, .001] if x<=t]))
rho.round(2).astype(str) + p

#%%
print(pg.multivariate_normality(engagement_sum_social_needs_sum_concat))
engagement_sum_social_needs_sum_concat.corr(method='spearman')

#%%
rho = engagement_sum_social_needs_sum_concat.corr(method='spearman')
pval = engagement_sum_social_needs_sum_concat.corr(method=lambda x, y: spearmanr(x, y)[1]) - np.eye(*rho.shape)
p = pval.applymap(lambda x: ''.join(['*' for t in [.05, .01, .001] if x<=t]))
rho.round(2).astype(str) + p


#%%

engagement_sum_social_needs_concat = pd.concat([engagement_sum, social_needs], axis=1) 
print(pg.multivariate_normality(engagement_sum_social_needs_concat))
engagement_sum_social_needs_concat.corr(method='spearman')

#%%
rho = engagement_sum_social_needs_concat.corr(method='spearman')
pval = engagement_sum_social_needs_concat.corr(method=lambda x, y: spearmanr(x, y)[1]) - np.eye(*rho.shape)
p = pval.applymap(lambda x: ''.join(['*' for t in [.05, .01, .001] if x<=t]))
rho.round(2).astype(str) + p


#%%
communication_mediums.corr(method='spearman')
#%%
rho = communication_mediums.corr(method='spearman')
pval = communication_mediums.corr(method=lambda x, y: spearmanr(x, y)[1]) - np.eye(*rho.shape)
p = pval.applymap(lambda x: ''.join(['*' for t in [.05, .01, .001] if x<=t]))
rho.round(2).astype(str) + p


#%%
social_needs.corr(method='spearman')
#%%
rho = social_needs.corr(method='spearman')
pval = social_needs.corr(method=lambda x, y: spearmanr(x, y)[1]) - np.eye(*rho.shape)
p = pval.applymap(lambda x: ''.join(['*' for t in [.05, .01, .001] if x<=t]))
rho.round(2).astype(str) + p

#%%
age_group_social_needs_sum_concat.corr(method='spearman')

#%%
rho = age_group_social_needs_sum_concat.corr()
pval = age_group_social_needs_sum_concat.corr(method=lambda x, y: spearmanr(x, y)[1]) - np.eye(*rho.shape)
p = pval.applymap(lambda x: ''.join(['*' for t in [.05, .01, .001] if x<=t]))
rho.round(2).astype(str) + p


#%%
communication_mediums_social_needs_concat.corr(method='spearman')

#%%
rho = communication_mediums_social_needs_concat.corr()
pval = communication_mediums_social_needs_concat.corr(method=lambda x, y: spearmanr(x, y)[1]) - np.eye(*rho.shape)
p = pval.applymap(lambda x: ''.join(['*' for t in [.05, .01, .001] if x<=t]))
rho.round(2).astype(str) + p

#%%
social_needs_important_customizations_concat.corr(method='spearman')

#%%
rho = social_needs_important_customizations_concat.corr()
pval = social_needs_important_customizations_concat.corr(method=lambda x, y: spearmanr(x, y)[1]) - np.eye(*rho.shape)
p = pval.applymap(lambda x: ''.join(['*' for t in [.05, .01, .001] if x<=t]))
rho.round(2).astype(str) + p

#%%
""" 

sns.pairplot(engagement_sum, kind='reg', diag_kind='kde',palette=colors)

sns.pairplot(engagement_sum_communication_mediums_other_concat, kind='reg', diag_kind='kde',palette=colors)
sns.pairplot(engagement_sum_communication_mediums_detractors_concat, kind='reg', diag_kind='kde',palette=colors)
sns.pairplot(engagement_sum_social_needs_sum_concat, kind='reg', diag_kind='kde',palette=colors)


sns.pairplot(communication_mediums_other_social_needs_sum_concat, kind='reg', diag_kind='kde',palette=colors)
sns.pairplot(communication_mediums_detractors_social_needs_loneliness_sum_concat, kind='reg', diag_kind='kde',palette=colors)
sns.pairplot(communication_mediums_detractors_social_needs_discussion_topics_sum_concat, kind='reg', diag_kind='kde',palette=colors)

sns.pairplot(social_needs_sum_important_customizations_concat, kind='reg', diag_kind='kde',palette=colors)
sns.pairplot(communication_mediums_important_customizations_concat, kind='reg', diag_kind='kde',palette=colors)
"""


""" 
office_visits_counts_daily_tools_usage_counts_concat = pd.concat([office_visits, daily_tools], axis=1)

print(pg.multivariate_normality(office_visits_counts_daily_tools_usage_counts_concat))
office_visits_counts_daily_tools_usage_counts_concat.corr(method='spearman')
"""

#%%
plt.show()
print("End of program")