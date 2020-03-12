
for i = 0, 7, 1 do

Trigger { -- Skill : Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
		Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
		Deaths(CurrentPlayer, Exactly, 1, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, i, " `UniqueSkill");
	},
	actions = {
		Comment("Skill : Unique");
		PreserveTrigger();
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		SetDeaths(CurrentPlayer, Add, 1, " `UniqueSkill");
		SetDeaths(CurrentPlayer, Add, 1, " `UniqueSkill");
	},
}
end