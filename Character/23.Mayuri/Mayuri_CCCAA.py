import Function as f;

const s = StringBuffer();

function main(cp)
{
   f.HoldPosition(cp);
   ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1);

   MoveUnit(All, "40 + 1n Marine", cp, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "40 + 1n Ghost", cp, "Anywhere", "[Skill]HoldPosition");

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {       
            SetDeaths(cp, SetTo, 1, " `ShieldRecharge");
            f.SquareShape(cp, 1, "40 + 1n Mutalisk", 50, 0);
            f.SquareShape(cp, 1, "40 + 1n Mutalisk", 100, 0);

            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {       
            f.SquareShape(cp, 1, "40 + 1n Mutalisk", 50, 50);
            f.SquareShape(cp, 1, "40 + 1n Mutalisk", 100, 100);

            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {       
            f.EdgeShape(cp, 1, "40 + 1n Guardian", 0, 5, 100);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {       
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 0, 7, 150);

            f.SquareShape(cp, 1, "40 + 1n Guardian", 200, 125);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 125, 200);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 200, 275);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 275, 200);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {       
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 200, 125);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 125, 200);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 200, 275);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 275, 200);
            f.SquareShape(cp, 1, "50 + 1n Tank", 200, 125);
            f.SquareShape(cp, 1, "50 + 1n Tank", 125, 200);
            f.SquareShape(cp, 1, "50 + 1n Tank", 200, 275);
            f.SquareShape(cp, 1, "50 + 1n Tank", 275, 200);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 150, 0);
            f.SquareShape(cp, 1, "50 + 1n Tank", 150, 0);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);

            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp);

            f.SkillWait(cp, 960);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 16)
         {        
            KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);

            if (f.loop[cp] % 3 == 0)
            {
               f.EdgeShape(cp, 1, "60 + 1n High Templar", 0, 7, 150);
               KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

               f.EdgeShape(cp, 1, "Target", 0, 5, 100);
               KillUnitAt(All, "Target", "Anywhere", cp);
            }

            MoveLocation(f.location[cp], "40 + 1n Marine", cp, "Anywhere");
            RemoveUnitAt(1, "40 + 1n Marine", "Anywhere", cp);

            CreateUnit(2, " Creep. Dunkelheit", "[Skill]Unit_Wait_1", cp);
            CreateUnit(6, "80 + 1n Vulture", "[Skill]Unit_Wait_1", cp);
            SetInvincibility(Enable, "80 + 1n Vulture", cp, "[Skill]Unit_Wait_ALL");
            SetInvincibility(Enable, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL");
            MoveUnit(2, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(6, "80 + 1n Vulture", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            KillUnitAt(All, "80 + 1n Vulture", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 16)
         {
            KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
            KillUnitAt(All, "80 + 1n Vulture", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         SetDeaths(cp, SetTo, 0, " `ShieldRecharge");
         KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp);
         f.SkillEnd(cp);
      }
   }
}