# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def grading(user_answers):
    correct_answers = {"NY": "Albany", "CA": "Sacramento", "AK": "Juneau", "FL": "Tallahassee", "WA": "Olympia"}
    result = {}
    for key, value in user_answers.items(): 
        if correct_answers[key] == value:
            result[key] = "Correct!"
        else:
            result[key] = user_answers[key] + "is incorrect! The correct answer is " + correct_answers[key]
    return result