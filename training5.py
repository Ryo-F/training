class Scout:
    def __init__(self, name, worker_type, skills, candidates=[]):
        self.skills = skills
        self.name = name
        self.worker_type = worker_type
        self.candidates = candidates

    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)

    def add_candidate(self, candidate):
        if candidate not in self.candidates:
            self.candidates.append(candidate)

    def get_candidate_name_list(self):
        return [self.candidates[i].name for i in range(len(self.candidates))]

    def search_candidate_or(self, skill_list):
        return [x.name for x in self.candidates if skill_list & set(x.skills)]

    def search_candidate_and(self, skill_list):
        return [i.name for i in self.candidates if skill_list & set(i.skills) == skill_list]


class Person:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
