import Function as f;

const s = StringBuffer();

function main(cp)
{
   f.BanReturn(cp);
   f.HoldPosition(cp);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 4)
         {         

            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 2 * f.loop[cp] + 1, 50);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            f.NxNSquareShape(cp, 1, "40 + 1n Guardian", 6, 75);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {
            f.SquareShape(cp, 1, "60 + 1n Siege", 114, 114);
            f.SquareShape(cp, 1, "60 + 1n Siege", 114, 190);
            f.SquareShape(cp, 1, "60 + 1n Siege", 190, 114);
            f.SquareShape(cp, 1, "60 + 1n Siege", 190, 190);
            f.SquareShape(cp, 1, "60 + 1n Siege", 38, 114);
            f.SquareShape(cp, 1, "60 + 1n Siege", 38, 175);
            f.SquareShape(cp, 1, "60 + 1n Siege", 114, 38);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 175, 38);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 114, 114);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 114, 190);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 190, 114);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 190, 190);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 38, 114);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 38, 175);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 114, 38);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 175, 38);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            f.SkillWait(cp, 720);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }

      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {         
            f.NxNSquareShape(cp, 1, "Kakaru (Twilight)", 3, 50);
            f.NxNSquareShape(cp, 1, "40 + 1n Goliath", 3, 50);
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, "Anywhere");
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 320);

            f.loop[cp] += 1;


         }
         else if (f.loop[cp] == 1)
         {         
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 0);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 50);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 100);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 150);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 200);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 150, 0);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 150, 50);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 150, 100);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 150, 150);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 150, 200);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 200, 0);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 200, 50);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 200, 100);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 200, 150);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 200, 200);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 50, 100);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 50, 150);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 50, 200);
            f.SquareShape(cp, 1, "40 + 1n Goliath", 175, 38);
            f.SquareShape(cp, 1, "40 + 1n Goliath", 114, 114);
            f.SquareShape(cp, 1, "40 + 1n Goliath", 114, 190);
            f.SquareShape(cp, 1, "40 + 1n Goliath", 190, 114);
            f.SquareShape(cp, 1, "40 + 1n Goliath", 190, 190);
            f.SquareShape(cp, 1, "40 + 1n Goliath", 38, 114);
            f.SquareShape(cp, 1, "40 + 1n Goliath", 38, 175);
            f.SquareShape(cp, 1, "40 + 1n Goliath", 114, 38);
            f.SquareShape(cp, 1, "40 + 1n Goliath", 175, 38);
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, "Anywhere");
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 320);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }

         
      }
      else if (f.count[cp] == 2)
      {
         if (Bring(cp, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill") && f.step[cp] == 210)
         {
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            f.Voice_Routine(cp, 4);
            f.wait[cp] = 0;
            f.count[cp] = 0;
            f.loop[cp] = 0;
            f.step[cp] = 220;
            KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", cp);
         }
         else 
         {
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
            f.SkillEnd(cp);
         }


      }


   }
}