import Function as f;

const s = StringBuffer();

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {                        
            f.SquareShape(cp, 1, "Target", 50, 50);
            f.SquareShape(cp, 1, " Creep. Dunkelheit", 50, 50);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);

            KillUnitAt(All, "Target", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {                 
            RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
            f.SquareShape(cp, 1, "Target", 50, 50);
            f.SquareShape(cp, 1, " Creep. Dunkelheit", 50, 50);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);

            KillUnitAt(All, "Target", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {            
            RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
            f.SquareShape(cp, 1, "Target", 50, 0);
            f.SquareShape(cp, 1, "Target", 100, 0);

            KillUnitAt(All, "Target", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {                 
            f.EdgeShape(cp, 1, "Protoss Dark Templar", 45, 5, 100);
            KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {                 
            f.EdgeShape(cp, 1, "40 + 1n Mutalisk", 0, 5, 100);
            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
            f.EdgeShape(cp, 1, "40 + 1n Ghost", 0, 3, 100);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {                 
            f.EdgeShape(cp, 1, "60 + 1n Danimoth", 0, 7, 150);
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
            f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 7, 150);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            f.EdgeShape(cp, 1, "Kakaru (Twilight)", 0, 5, 100);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }


      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 4)
         {         
            f.DotShape(cp, 1, "Protoss Dark Templar", 100 - 25 * f.loop[cp], 25 * f.loop[cp]);
            f.DotShape(cp, 1, "Protoss Dark Templar", -100 + 25 * f.loop[cp], -25 * f.loop[cp]);
            f.DotShape(cp, 1, "40 + 1n Zealot", -25 * f.loop[cp], 100 - 25 * f.loop[cp]);
            f.DotShape(cp, 1, "40 + 1n Zealot", 25 * f.loop[cp], -100 + 25 * f.loop[cp]);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp);

            f.SkillWait(cp, 320);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] == 0)
         {
            f.Voice_Routine(cp, 2);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 75, 150);
            f.SquareShape(cp, 1, "60 + 1n Archon", 50, 100);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 150, 75);
            f.SquareShape(cp, 1, "60 + 1n Archon", 100, 50);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 75, 150);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 50, 100);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 150, 75);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 100, 50);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Ghost", 50, 100);
            f.SquareShape(cp, 1, "40 + 1n Ghost", 100, 50);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {                 
            f.SquareShape(cp, 1, "40 + 1n Mutalisk", 50, 0);
            f.SquareShape(cp, 1, "40 + 1n Mutalisk", 100, 0);

            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {                 
            f.SquareShape(cp, 1, "40 + 1n Guardian", 50, 100);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 100, 50);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {                 
            KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp);

            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 75, 150);
            f.SquareShape(cp, 1, "40 + 1n Ghost", 75, 150);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 150, 75);
            f.SquareShape(cp, 1, "40 + 1n Ghost", 150, 75);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 320);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 3)
      {
         KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp);
         f.SkillEnd(cp);
      }
   }
}