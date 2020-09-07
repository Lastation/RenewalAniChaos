

for i = 0, 3, 1 do

distance = 100;
radius = (i + 1) / 8 * math.pi;

x = math.sin(radius) * distance;
y = math.cos(radius) * distance;

x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "Protoss Dark Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -y, x);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, y, -x);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
   },
}


x = 100;
y = 100;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnitWithProperties(3, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer, {
         clocked = true,
         burrowed = false,
         intransit = false,
         hallucinated = false,
         invincible = false,
         hitpoint = 100,
         shield = 100,
         energy = 100,
         resource = 0,
         hanger = 0,
      });  
      CreateUnit(3, "Protoss Dark Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, 0, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger(); 
      CreateUnit(3, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, 0, 0);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnitWithProperties(3, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer, {
         clocked = true,
         burrowed = false,
         intransit = false,
         hallucinated = false,
         invincible = false,
         hitpoint = 100,
         shield = 100,
         energy = 100,
         resource = 0,
         hanger = 0,
      });  
      CreateUnit(3, "Protoss Dark Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, 0, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger(); 
      CreateUnit(3, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, y);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, -y);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, 0, 0);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnitWithProperties(3, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer, {
         clocked = true,
         burrowed = false,
         intransit = false,
         hallucinated = false,
         invincible = false,
         hitpoint = 100,
         shield = 100,
         energy = 100,
         resource = 0,
         hanger = 0,
      });  
      CreateUnit(3, "Protoss Dark Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, 0, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, 0, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, 0, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger(); 
      CreateUnit(3, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, 0, y);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, 0, -y);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, 0, 0);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnitWithProperties(3, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer, {
         clocked = true,
         burrowed = false,
         intransit = false,
         hallucinated = false,
         invincible = false,
         hitpoint = 100,
         shield = 100,
         energy = 100,
         resource = 0,
         hanger = 0,
      });  
      CreateUnit(3, "Protoss Dark Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger(); 
      CreateUnit(3, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, -y);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, 0);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnitWithProperties(3, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer, {
         clocked = true,
         burrowed = false,
         intransit = false,
         hallucinated = false,
         invincible = false,
         hitpoint = 100,
         shield = 100,
         energy = 100,
         resource = 0,
         hanger = 0,
      });  
      CreateUnit(3, "Protoss Dark Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, 0);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger(); 
      CreateUnit(3, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, y);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, 0);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
   },
}

for i = 0, 3, 1 do

distance = 100;
radius = (i + 1) / 8 * math.pi;

x = math.sin(radius) * distance;
y = math.cos(radius) * distance;

x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "Protoss Dark Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -y, x);
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, y, -x);
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

x = 0;
y = 0;
interval = 75;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(350);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, interval);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, 0);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, 0);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, -interval);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, -interval);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(500);
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}