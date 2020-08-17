
Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
   },
   actions = {
      Comment("Skill : Ulitmate");
      PreserveTrigger();
      CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro_Bozo", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      Order(" * Samir Duran", CurrentPlayer, "Anywhere", Move, "14.Yashiro_Bozo");
      KillUnit("Protoss Observer", CurrentPlayer);
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop4");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
      Deaths(CurrentPlayer, AtMost, 7, " `UniqueSkill");
   },
   actions = {
      Comment("Skill : Ulitmate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, Add, 1, " `UniqueSkill");
      SetDeaths(CurrentPlayer, Subtract, 80, " `UltimateCoolTime");
   },
}

for i = 0, 7, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 1, " `UniqueSkill");
   },
   actions = {
      Comment("Skill : Ulitmate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop4");
      Deaths(CurrentPlayer, Exactly, 8, " `UniqueSkill");
   },
   actions = {
      Comment("Skill : Ulitmate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 201, " `SkillLoop4");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 199, " `SkillLoop4");
      Deaths(CurrentPlayer, Exactly, 8, " `UniqueSkill");
   },
   actions = {
      Comment("Skill : Ulitmate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}
