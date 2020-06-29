

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, AtMost, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, "Any unit", "[Skill]Hallu_Bozo");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "Any unit", "[Skill]Hallu_Bozo", CurrentPlayer);
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, AtLeast, 110, " `SkillStep");
      Bring(CurrentPlayer, Exactly, 0, "40 + 1n Drone", "[Skill]Hallu_Bozo");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(1, "40 + 1n Drone", "[Skill]Hallu_Bozo", CurrentPlayer);
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
      MoveUnit(All, "40 + 1n Drone", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
      KillUnit("Protoss Observer", CurrentPlayer);
      CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      Order(" * Samir Duran", CurrentPlayer, "Anywhere", Move, "20.EmetSelch");      
   },
}

for i = 0, 5, 1 do

x = 225 - 75 * i;
y = 150 - 75 * i;


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(2, "80 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnitWithProperties(2, "40 + 1n Drone", "[Skill]Unit_Wait_8", CurrentPlayer, {
         clocked = false,
         burrowed = true,
         intransit = false,
         hallucinated = true,
         invincible = false,
         hitpoint = 100,
         shield = 100,
         energy = 100,
         resource = 0,
         hanger = 0,
      });  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x, -y);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(All, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 5, 1 do

x = 150 - 75 * i;
y = -225 + 75 * i;


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(2, "80 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnitWithProperties(2, "40 + 1n Drone", "[Skill]Unit_Wait_8", CurrentPlayer, {
         clocked = false,
         burrowed = true,
         intransit = false,
         hallucinated = true,
         invincible = false,
         hitpoint = 100,
         shield = 100,
         energy = 100,
         resource = 0,
         hanger = 0,
      });  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x, -y);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(All, "40 + 1n Drone", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


for i = 0, 5, 1 do

x = 225 - 75 * i;
y = 150 - 75 * i;


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(2, "80 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x, -y);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end


for i = 0, 5, 1 do

x = 150 - 75 * i;
y = -225 + 75 * i;


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 6, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(2, "80 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x, -y);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end
Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Guardian", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(300);
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      Order("40 + 1n Drone", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(2500);
      SetDeaths(AllPlayers, SetTo, 2001, " `SkillText4");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}


for i = 0, 3, 1 do


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop2");
      Bring(CurrentPlayer, AtLeast, 1, "40 + 1n Drone", "Anywhere");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(1, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(1, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "40 + 1n Drone", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "40 + 1n Drone", "Anywhere", CurrentPlayer);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(3400);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

Trigger { -- Skill : Use Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Bring(CurrentPlayer, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill");
      Bring(CurrentPlayer, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill");
   },
   actions = {
      Comment("Skill : Use Combo");
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop");
      Wait(500);
      SetDeaths(AllPlayers, SetTo, 2002, " `SkillText4");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 120, " `SkillStep");
      KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
      KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
      PreserveTrigger();
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}